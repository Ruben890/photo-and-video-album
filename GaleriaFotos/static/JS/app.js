const archivo_img = document.getElementById("id_img");
const archivo_video = document.getElementById("id_video");

const btn_archivo = document.getElementById("btn_img");
const btn_archivo_vid = document.getElementById("btn_video");

//*carga de imagenes
btn_archivo.addEventListener("click", (e) => {
  e.preventDefault();
  archivo_img.click();
});

archivo_img.addEventListener("change", () => {
  for (let i = 0; i < archivo_img.files.length; i++) {
    const element = URL.createObjectURL(archivo_img.files[i]);
    const img = document.createElement("img");
    img.src = element;
    document.querySelector(".img_contents").appendChild(img);
  }
});

//*cargar videos
btn_archivo_vid.addEventListener("click", (e) => {
  e.preventDefault();
  archivo_video.click();
});

archivo_video.addEventListener("change", () => {
  for (let i = 0; i < archivo_video.files.length; i++) {
    const element = URL.createObjectURL(archivo_video.files[i]);
    const video = `<video src="${element}" controls></video>`;
    document.querySelector(".video_contents").innerHTML = video;
  }
});
