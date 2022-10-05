fetch(
	"https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
)
	.then(function (response) {
		return response.json();
	})
	.then(function (data) {
		let webData = data["result"]["results"];
		let myData = {};
		let myArray = [];

		for (let item of webData) {
			let itemFile = item["file"];
			splitUrl = itemFile.split("https://");
			firstUrl = "https://" + splitUrl[1];

			let placeName = item["stitle"];

			myData = {
				placeName: placeName,
				firstUrl: firstUrl,
			};
			myArray.push(myData);
		}
		let smallDiv = myArray.slice(0, 2);
		let bigDiv = myArray.slice(2, 10);
		let moreDiv = myArray.slice(10, 58);
		let section = document.querySelector("section .section-container");
		let add = document.querySelector("div button");

		smallDiv.forEach((item) => {
			let imgs = document.createElement("img");
			imgs.classList.add("img-item-1");
			imgs.src = item.firstUrl;
			let p = document.createElement("p");
			p.innerText = item.placeName;

			let div = document.createElement("div");
			div.classList.add("item-container-1");
			div.appendChild(imgs);
			div.appendChild(p);
			section.appendChild(div);
		});
		bigDiv.forEach((item) => {
			let imgs = document.createElement("img");
			imgs.classList.add("img-item-2");
			imgs.src = item.firstUrl;
			let p = document.createElement("p");
			p.classList.add("item-p");
			p.innerText = item.placeName;

			let div = document.createElement("div");
			div.classList.add("item-container-2");
			div.appendChild(imgs);
			div.appendChild(p);
			section.appendChild(div);
		});

		moreDiv.forEach((item) => {
			let imgs = document.createElement("img");
			imgs.classList.add("img-item-2");
			imgs.src = item.firstUrl;
			let p = document.createElement("p");
			p.classList.add("item-p");
			p.innerText = item.placeName;

			let div = document.createElement("div");
			div.classList.add("item-container-2");
			div.classList.add("toggle");
			div.appendChild(imgs);
			div.appendChild(p);
			section.appendChild(div);
		});
		let hideDiv = document.querySelectorAll("section .item-container-2");

		let showDiv = 8;
		add.addEventListener("click", (e) => {
			e.preventDefault();
			for (let i = showDiv; i < showDiv + 8; i++) {
				if (hideDiv[i]) {
					hideDiv[i].style.display = "block";
				}
			}
			showDiv += 8;

			if (showDiv >= hideDiv.length) {
				e.target.style.display = "none";
			}
		});
	});
