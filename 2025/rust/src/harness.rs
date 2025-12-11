use std::{env, fs, path::Path};

use reqwest::{
    self,
    header::{COOKIE, HeaderValue},
};

pub fn extract_day(file_name: &str) -> usize {
    let day_as_str = file_name
        .rsplit('/')
        .next()
        .and_then(|s| s.strip_prefix("day"))
        .and_then(|s| s.strip_suffix(".rs"))
        .expect("file name must be of the form …/dayX.rs");
    let day_as_usize = day_as_str.parse::<usize>().unwrap();
    return day_as_usize;
}

// explanation: format! expects a literal. You cannot define global literals. This is a workaround.
// Keeping it here for educational purposes, instead of using replace instead of format.
macro_rules! url_template {
    () => {
        "https://adventofcode.com/{year}/day/{day}/input"
    };
}
const YEAR: usize = 2025;

pub fn get_input(day: usize) -> String {
    get_from_cache(day).unwrap_or_else(|| get_from_online(day))
}

pub fn get_from_online(day: usize) -> String {
    let user_agent = env::var("USERAGENT").unwrap();
    let session = env::var("SESSION").unwrap();
    let client = reqwest::blocking::Client::new();
    let request = client
        .get(format!(url_template!(), year = YEAR, day = day))
        .header(
            reqwest::header::HeaderName::from_static("user-agent"),
            HeaderValue::from_str(&user_agent).unwrap(),
        )
        .header(COOKIE, format!("session={session}"))
        .build();

    let body = client.execute(request.unwrap()).unwrap().text().unwrap();
    save_to_cache(&body, day);
    return body;
}

pub fn get_from_cache(day: usize) -> Option<String> {
    return fs::read_to_string(format!("tmp/day{}.txt", day)).ok();
}

pub fn save_to_cache(text: &str, day: usize) {
    fs::write(Path::new(&format!("tmp/day{}.txt", day)), text.as_bytes()).unwrap()
}
