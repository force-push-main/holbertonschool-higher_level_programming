// const toRed = () => {
//   const element = document.querySelector('header');
//   element.style.color = '#FF0000';
// };

// ------ alternate method of changing colour using event listener ------

const header = document.querySelector('header');
const red_header = document.querySelector('#red_header');
red_header.addEventListener('click', () => {
  header.style.color = '#FF0000';
});
