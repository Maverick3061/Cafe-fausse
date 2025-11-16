import React, { useState } from "react";
import "./Gallery.css";
import Lightbox from "yet-another-react-lightbox";
import "yet-another-react-lightbox/styles.css";

const Gallery = () => {
  const images = [
    { src: "/Project/interior.jpg" },
    { src: "/Project/dish1.jpg" },
    { src: "/Project/dish2.jpg" },
    { src: "/Project/cafe-fausse.jpg" },
  ];

  const [open, setOpen] = useState(false);
  const [index, setIndex] = useState(0);

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h2 className="text-3xl font-bold text-center mb-8">Our Gallery</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {images.map((img, i) => (
          <div
            key={i}
            className="overflow-hidden rounded-2xl shadow-md cursor-pointer transform hover:scale-105 transition"
            onClick={() => { setIndex(i); setOpen(true); }}
          >
            <img
              src={img.src}
              alt={`Gallery ${i + 1}`}
              className="w-full h-64 object-cover"
            />
          </div>
        ))}
      </div>

      {open && (
        <Lightbox
          open={open}
          close={() => setOpen(false)}
          index={index}
          slides={images}
        />
      )}
    </div>
  );
};

export default Gallery;
