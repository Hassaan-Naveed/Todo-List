
export default async function Home() {
  const data = await fetch(`${process.env.LOCAL_SERVER}/api/todos/`)
  const todos = await data.json()

  return (
    <div>
      <h1>Todo List 123</h1>
        <ul>
          {todos.map((todo) => (
            <li key={todo.id}>{todo.title}</li>
          ))}
        </ul>
    </div>
  );
}
