// const updateHeader = () => {
//   document.querySelector('#update_header').textContent = 'New Header!!';
// };

// ------ alternate method of updating header using add event listener and callback function --------

const updateHeaderCallback = () => {
  document.querySelector('header').textContent = 'New Header!!';
};

const updateHeaderEl = document.querySelector('#update_header');
updateHeaderEl.addEventListener('click', updateHeaderCallback);

const updateHeader = () => null;
