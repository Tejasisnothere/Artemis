import express from "express";

import authRoutes from "./routes/auth.routes.js";
import fileRoutes from "./routes/file.routes.js";
import organisationRoutes from "./routes/organisation.routes.js";
import productRoutes from "./routes/product.routes.js";
import reviewRoutes from "./routes/review.routes.js";

const app = express();

app.use(express.json);

app.use("/api/auth", authRoutes);
app.use("/api/files", fileRoutes);
app.use("/api/organisation", organisationRoutes);
app.use("/api/products", productRoutes);
app.use("/api/reviews", reviewRoutes);

app.listen(8000, () => {
    console.log("Hello from the server pookie");
});