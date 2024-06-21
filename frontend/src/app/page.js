import CardBlog from "@/components/CardBlog";
import Header from "@/components/Header";
import style from "./page.module.css"

export default function Home() {
  return (
    <main>
      <Header />
      <div className={style.centralize}>
        <CardBlog />
      </div>
    </main>
  );
}