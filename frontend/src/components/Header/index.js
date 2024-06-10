import style from "./header.module.css";
import Link from "next/link";
import ProfileIcon from "../ProfileIcon";

export default function Header() {
  return (
    <header className={style.container}>
      <h1 className={style.logo}>Libs</h1>
      <nav className={style.nav}>
        <Link className={style.navItem} href="Livros">
          Livros
        </Link>
        <Link className={style.navItem} href="Salvos">
          Salvos
        </Link>
        <Link className={style.navItem} href="Blogs">
          Blogs
        </Link>
        <div className={style.icon}>
          <ProfileIcon />
        </div>
      </nav>
    </header>
  );
}
