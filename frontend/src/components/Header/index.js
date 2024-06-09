import style from "./header.module.css";
import Link from "next/link";

export default function Header() {
  return (
    <header className={style.container}>
      <h1>Libs</h1>
      <nav className={style.nav}>
        <Link className={style.nav} href="Livros">
          Livros
        </Link>
        <Link className={style.nav} href="Salvos">
          Salvos
        </Link>
        <Link className={style.nav} href="Blogs">
          Blogs
        </Link>
        <div className="icon">
          <svg
            width="29"
            height="29"
            viewBox="0 0 29 29"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <rect
              x="0.5"
              y="0.5"
              width="27.59"
              height="27.59"
              fill="#FF964A"
              stroke="black"
            />
            <path
              d="M26.3024 19.72C26.3024 21.7745 21.0229 23.44 14.5104 23.44C7.99785 23.44 2.71838 21.7745 2.71838 19.72C2.71838 17.6655 7.99785 16 14.5104 16C21.0229 16 26.3024 17.6655 26.3024 19.72Z"
              fill="black"
            />
            <ellipse cx="14.6619" cy="9" rx="5.94356" ry="5" fill="black" />
          </svg>
        </div>
      </nav>
    </header>
  );
}
