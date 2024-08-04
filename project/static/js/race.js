$(document).ready(function () {
  let input_text = document.getElementById("input_text");
  let word_to_type_holder = document.getElementById("word_to_type_holder");
  let text_to_type_element = document.getElementById("text_to_type");
  let remaining_time = document.getElementById("remaining_time");
  let score_holder = document.getElementById("score_holder");
  let try_again_btn = document.getElementById("try_again_btn");
  let score_holder_h3 = document.getElementById("score_holder_h3");
  let timer_holder = document.getElementById("timer_holder");
  let remaining_time_h3 = document.getElementById("remaining_time_h3");
  let body_content = document.getElementById("body_content");
  let text_to_type = text_to_type_element.textContent;
  let words = text_to_type.split(/(\s+)/);
  let current_word_index = 0;
  let minutes = 4;
  let seconds = minutes * 60;
  remaining_time.innerText = `4:00`;
  let correct_word_per_minute = 0;
  let time_elapsed = 0;
  let total_correct_words = 0;
  let start_timer = 6;
  let interval;
  let timer_interval;
  let should_take_input = true;
  let span = timer_holder.querySelector("span");
  span.innertText = `${start_timer} Sec`;

  //show timer of race starting
  timer_interval = setInterval(function () {
    start_timer--;
    span.innerText = start_timer + " seconds";
    if (start_timer <= 0) {
      clearInterval(timer_interval);
      interval = setInterval(updateTimer, 1000);
      timer_holder.classList.toggle("hide");
      remaining_time_h3.classList.toggle("hide");
      input_text.disabled = false;
    }
  }, 1000);

  //update timer

  function updateTimer() {
    if (seconds <= 0) {
      clearInterval(interval);
      alert("Time's up!");
      input_text.disabled = true;
      try_again_btn.classList.toggle("show");
      return;
    }
    seconds--;
    time_elapsed++;
    let elapsed_minutes = Math.floor(time_elapsed / 60);
    if (elapsed_minutes >= 1) {
      score_holder.innerText = `${correct_word_per_minute} wpm`;
      time_elapsed = 0;
      correct_word_per_minute = 0;
    }

    let display_minutes = Math.floor(seconds / 60);

    let display_seconds = seconds % 60;

    remaining_time.innerText =
      display_minutes +
      ":" +
      (display_seconds < 10 ? "0" : "") +
      display_seconds;
  }

  //restart the race
  try_again_btn.addEventListener("click", function () {
    alert("clicked");
    this.classList.toggle("hide");
    timer_holder.classList.toggle("hide");
    remaining_time_h3.classList.toggle("hide");
    minutes = 4;
    seconds = minutes * 60;
    total_correct_words = 0;
    current_word_index = 0;
  });

  function updateWords() {
    if (current_word_index < words.length) {
      // Join the current word with the following space (if any)
      let current_word = words[current_word_index];
      if (
        current_word_index + 1 < words.length &&
        words[current_word_index + 1] === " "
      ) {
        current_word += " ";
      }
      word_to_type_holder.innerText = current_word;
      word_to_type_holder.style.color = "green";
      word_to_type_holder.style.textDecoration = "underline";
      text_to_type_element.innerText = words
        .slice(current_word_index + 1)
        .join("");
    } else {
      word_to_type_holder.innerText = "You finished!";
      clearInterval(interval);
      let time_taken_to_finish = minutes * 60 - seconds; //calculating time taken to finish typing all words
      let taken_minutes = time_taken_to_finish / 60;
      let average_words_per_minutes = Math.floor(
        total_correct_words / taken_minutes
      );

      score_holder.innerText = `${average_words_per_minutes} wpm`;
      score_holder_h3.innerText = `Average wpm is ${average_words_per_minutes}`;
      text_to_type_element.innerText = "";
    }
  }

  updateWords();

  input_text.addEventListener("input", function (e) {
    if (!should_take_input) {
      let current_value = input_text.value;
      let new_value = e.data;
      if (new_value != null) {
        input_text.value = current_value.slice(0, -new_value.length); //remove the new added input value
      }
      body_content.style.position = "relative";
      $("#errorModal").modal("show");

      return;
    }
    let typed_word = input_text.value;

    let current_word = words[current_word_index];
    if (
      current_word_index + 1 < words.length &&
      words[current_word_index + 1] === " "
    ) {
      current_word += " ";
    }

    if (typed_word === current_word) {
      correct_word_per_minute++;
      total_correct_words++;
      console.log("matched");
      current_word_index += current_word.endsWith(" ") ? 2 : 1; // Move to next word, skip space if needed
      updateWords();
      input_text.value = "";
    } else if (current_word.startsWith(typed_word)) {
      console.log("partial match");
    } else {
      if (typed_word.length >= 2) {
        for (var i = 0; i < typed_word.length; i++) {
          if (typed_word[i] === current_word[i]) {
            console.log("equal");
          } else {
            console.log("not equal");
          }
        }
        should_take_input = false;
        input_text.classList.add("invalid");
      }
      console.log("not matched");
    }
  });
});
