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
            const options = data.map((item) => {
              return `<option value=${item.id}>${item.nombre}</option>`});
            options.unshift('<option value="">---------</option>')
            document.getElementById("id_comuna").innerHTML = options
          });
      });
  },
  false
);