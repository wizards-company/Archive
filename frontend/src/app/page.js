import CardBlog from "@/components/CardBlog";
import Header from "@/components/Header";
import style from "./page.module.css"
import CardBook from "@/components/CardBook";

export default function Home() {
  return (
    <main>
      <Header />
      <div className={style.centralize}>
        <CardBlog />
      </div>
      <div className={style.centralize}>
        <CardBook />
      </div>
    </main>
  );
}