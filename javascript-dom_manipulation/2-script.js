// const changeColor = () => {
//   const header = document.querySelector('header');
//   header.className = 'red';
// };

// ---- alternate method for updating classname using add event listener -----

const header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');
redHeader.addEventListener('click', () => {
  header.className = 'red';
});

// here to prevent reference error

const changeColor = () => null;
