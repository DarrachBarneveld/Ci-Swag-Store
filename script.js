function humanReadable(seconds) {
  let numSecs = +seconds;
  let hours = Math.floor(numSecs / 3600);
  let minutes = Math.floor((numSecs % 3600) / 60);
  let remainingSeconds = numSecs % 60;

  hours = hours < 10 ? `0${hours}` : hours;
  minutes = minutes < 10 ? `0${minutes}` : minutes;
  remainingSeconds =
    remainingSeconds < 10 ? `0${remainingSeconds}` : remainingSeconds;

  return `${hours}:${minutes}:${remainingSeconds}`;
}

console.log(humanReadable(359999));
