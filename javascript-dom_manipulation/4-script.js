// const addItem = () => {
//   const listEl = document.querySelector('.my_list');
//   listEl.innerHTML += '<li>Item</li>';
// };

// ---- alternate method for adding li item using addevent listener -----

const addItemEl = document.querySelector('#add_item');
addItemEl.addEventListener('click', () => {
  const listEl = document.querySelector('.my_list');
  listEl.innerHTML += '<li>Item</li>';
});

// ---- here to prevent reference error

const addItem = () => null;
