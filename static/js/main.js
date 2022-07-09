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
            var options = '<option value="">---------</option>';
            data.map((item) => {
              options +=
                '<option value="' + item.id + '">' + item.nombre + "</option>";
            });
            document.getElementById("id_comuna").innerHTML = options;
          });
      });
  },
  false
);
