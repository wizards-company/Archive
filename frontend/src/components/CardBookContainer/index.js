import Button from "../Button"
import style from "./card.module.css"
import Container from "../Container"
import CardBook from "../CardBook"
export default function CardBookContainer() {
  const books = [1, 2, 3, 4, 5, 6, 7, 8]
  return (
    <Container>
      <div className={style.container}>
        {books.map((item, id) => (
          <CardBook />
        ))}
        <div className={style.div}>
          <Button
            text="Ver todos os livros"
            variant="blue"
            textColor="--base-white"
          />
        </div>
      </div>
    </Container>
  )
}
