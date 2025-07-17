const fetchData = async () => {
  try {
    const res = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
    const data = await res.json();
    return data;
  } catch {
    console.log('something went wrong');
  }
};

window.addEventListener('load', async () => {
  const data = await fetchData();
  document.querySelector('#hello').textContent = data.hello;
});
