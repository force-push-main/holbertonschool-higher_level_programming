const fetchData = async () => {
  try {
    const res = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
    const data = await res.json();
    return data.results;
  } catch {
    console.log('something went wrong');
  }
};

window.addEventListener('load', async () => {
  const list_movies = document.querySelector('#list_movies');
  const data = await fetchData();
  data.forEach((el) => {
    list_movies.innerHTML += `<li>${el.title}</li>`;
  });
});
