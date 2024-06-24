import CardBlog from "@/components/CardBlog";
import style from "./page.module.css"
import CardBook from "@/components/CardBook";

export default function Home() {
  return (
    <main>
      <CardBlog />
      <CardBook />
    </main>
  );
}