const toggleColor = () => {
  const header = document.querySelector('header');
  if (header.className === 'green') {
    header.className = 'red';
  } else {
    header.className = 'green';
  }
};
