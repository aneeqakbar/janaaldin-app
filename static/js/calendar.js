let date = new Date();
let year = date.getFullYear();
let month = date.getMonth();

let selectedDate = new Date();

function getValidMonth(month) {
  if(Number(month) >= 12) {
    return 0
  } else if(Number(month) < 0) {
    return 11
  }
  return Number(month)
}

function hasClass(dateString) {
  if(!CLASS_DATA) return false;

  for(let i = 0; i < CLASS_DATA?.available_times?.length; i++) {
    const time = CLASS_DATA?.available_times[i];

    const classDate = new Date(time.datetime);
    const currentDate = new Date(dateString);

    // let dateParts = String(dateString).split("-")
    // let currentDate = new Date(year=dateParts[0], month=dateParts[1], date=dateParts[2]);

    if(
      classDate.getDate() === currentDate.getDate() &&
      classDate.getMonth() === currentDate.getMonth() &&
      classDate.getFullYear() === currentDate.getFullYear()
    ) {
      return true;
    }
  }

  return false;
}

function updateServiceDetails() {
  if(!CLASS_DATA) return false;

  const serviceDetails = document.getElementById("service-details");
  const content = serviceDetails.querySelector(".content")

  content.innerHTML = "";

  const serviceCont = document.createElement("div")
  serviceCont.classList.add("my-3", "service")

  serviceCont.innerHTML = `
    <p class="mb-0">${CLASS_DATA?.name}</p>
    <p class="mb-2">${days[selectedDate.getDay()]}, ${months[selectedDate.getMonth()]} ${selectedDate.getDate()}</p>

    <p class="text-muted">
      <small>Online meetup<br>1hr</small>
    </p>
  `

  content.appendChild(serviceCont)
}

const day = document.querySelector(".calendar-dates");

const currdate = document
  .querySelector(".calendar-current-date");

const prenexIcons = document
  .querySelectorAll(".calendar-navigation span");

// Array of month names
const months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
];
const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];


// Function to generate the calendar
const manipulate = () => {

  // Get the first day of the month
  let dayone = new Date(year, month, 1).getDay();

  // Get the last date of the month
  let lastdate = new Date(year, month + 1, 0).getDate();

  // Get the day of the last date of the month
  let dayend = new Date(year, month, lastdate).getDay();

  // Get the last date of the previous month
  let monthlastdate = new Date(year, month, 0).getDate();

  // Variable to store the generated calendar HTML
  let lit = "";

  // Loop to add the last dates of the previous month
  for(let i = dayone; i > 0; i--) {
    lit +=
      `<li data-date="${year}-${getValidMonth(month - 1)}-${monthlastdate - i + 1}" class="inactive">${monthlastdate - i + 1}</li>`;
  }

  // Loop to add the dates of the current month
  for(let i = 1; i <= lastdate; i++) {

    // Check if the current date is today
    // let isToday = i === date.getDate()
    // 	&& month === new Date().getMonth()
    // 	&& year === new Date().getFullYear()
    // 	? "active"
    // 	: "";

    const dateString = `${year}-${month}-${i}`;

    let isSelected = i === selectedDate.getDate()
      && month === selectedDate.getMonth()
      && year === selectedDate.getFullYear()
      ? "active"
      : "";

    // console.log(dateString)

    const isActive = hasClass(`${year}-${month + 1}-${i}`);
    // console.log(isActive)

    lit += `
    <li data-date="${dateString}" class="${isSelected}">
      ${i}
      ${isActive ? '<span class="active-dot"></span>' : ''}
    </li>`;
  }

  // Loop to add the first dates of the next month
  for(let i = dayend; i < 6; i++) {
    lit += `<li data-date="${year}-${getValidMonth(month + 1)}-${i - dayend + 1}" class="inactive">${i - dayend + 1}</li>`
  }

  // Update the text of the current date element
  // with the formatted current month and year
  currdate.innerText = `${months[month]} ${year}`;

  // update the HTML of the dates element
  // with the generated calendar
  day.innerHTML = lit;

  const dateDisplay = document.querySelector(".main-cont .main-time-cont .date-display")
  dateDisplay.innerText = `${days[selectedDate.getDay()]}, ${months[selectedDate.getMonth()]} ${selectedDate.getDate()}`;


  const mainTimeCont = document.querySelector(".main-cont .main-time-cont .content")
  mainTimeCont.innerHTML = ""

  for(let i = 0; i < CLASS_DATA?.available_times?.length; i++) {
    const time = CLASS_DATA?.available_times[i];

    const classDate = new Date(time.datetime);

    if(
      classDate.getDate() === selectedDate.getDate() &&
      classDate.getMonth() === selectedDate.getMonth() &&
      classDate.getFullYear() === selectedDate.getFullYear()
    ) {
      classDate.setSeconds(0)

      const timeCont = document.createElement("div")
      timeCont.classList.add("time-cont")
      timeCont.innerText = classDate.toLocaleTimeString()
    
      mainTimeCont.appendChild(timeCont)
    }
  }

  initializeEvents()

}

manipulate();

// Attach a click event listener to each icon
prenexIcons.forEach(icon => {

  // When an icon is clicked
  icon.addEventListener("click", () => {

    // Check if the icon is "calendar-prev"
    // or "calendar-next"
    month = icon.id === "calendar-prev" ? month - 1 : month + 1;

    // Check if the month is out of range
    if(month < 0 || month > 11) {

      // Set the date to the first day of the
      // month with the new year
      date = new Date(year, month, new Date().getDate());

      // Set the year to the new year
      year = date.getFullYear();

      // Set the month to the new month
      month = date.getMonth();
    }

    else {

      // Set the date to the current date
      date = new Date();
    }

    // Call the manipulate function to
    // update the calendar display
    manipulate();
  });
});

function initializeEvents() {
  const singleDays = document.querySelectorAll(".calendar-dates li:not(.inactive)");
  const availableTimes = document.querySelectorAll(".main-cont .main-time-cont .content .time-cont")

  singleDays.forEach(day => {
    day.addEventListener("click", () => {
      const dateParts = day.getAttribute("data-date").split("-")
      const date = new Date(dateParts[0], dateParts[1], dateParts[2])
      selectedDate = date;
      manipulate();
    })
  });

  availableTimes.forEach(timeCont => {
    timeCont.addEventListener("click", () => {

      availableTimes.forEach(timeCont => {
        timeCont.classList.toggle("selected", false);
      });

      timeCont.classList.toggle("selected", true);

      updateServiceDetails()

    })
  });
}
