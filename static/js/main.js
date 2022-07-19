document.addEventListener(
  "DOMContentLoaded",
  function () {
    document
      .getElementById("id_region")
      .addEventListener("change", function () {
        fetch(
          "/get_comuna/?" +
            new URLSearchParams({
              id: this.value,
            }).toString()
        )
          .then((res) => res.json())
          .then(function (data) {    
            document.getElementById("id_comuna").innerHTML = data.map((item) => {
              return `<option value=${item.id}>${item.nombre}</option>`
            });
          });
      });
  },
  false
);