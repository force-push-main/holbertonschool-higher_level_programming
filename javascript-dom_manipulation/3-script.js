// ----- creates toggle feature using HTML's native onClick method -----

// const toggleColor = () => {
//   const header = document.querySelector('header');
//   if (header.className === 'green') {
//     header.className = 'red';
//   } else {
//     header.className = 'green';
//   }
// };

// ----- alternate toggle method using event listener -------

const header = document.querySelector('header');
const toggleButton = document.querySelector('#toggle_header');
toggleButton.addEventListener('click', () => {
  if (header.className === 'green') {
    header.className = 'red';
  } else {
    header.className = 'green';
  }
  console.log('event listener fired');
});

// ------ here to prevent reference error -------

const toggleColor = () => {
  return;
};
