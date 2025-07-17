const fetchData = async () => {
  try {
    const res = await fetch(
      'https://swapi-api.hbtn.io/api/people/5/?format=json'
    );
    const data = await res.json();
    return data.name;
  } catch {
    console.log('something went wrong');
  }
};

window.addEventListener('load', async () => {
  const name = await fetchData();
  document.querySelector('#character').textContent = name;
});
