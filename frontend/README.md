# Frontend — Score → Explain → Act UI

A single-screen React + Vite app for exercising the scoring API. Enter a salary-advance
request, hit **Get score**, and view the risk score, band, top drivers, policy citation,
recommended action, and the raw JSON response.

## Run
```bash
npm install
npm run dev        # http://localhost:5173
```

The API base URL defaults to `http://127.0.0.1:8000` and can be overridden with
`VITE_API_BASE` (see `.env.example`). Start the backend first (see `../backend`).

## Scripts
- `npm run dev` — dev server with HMR
- `npm run build` — production build to `dist/`
- `npm run lint` — ESLint
