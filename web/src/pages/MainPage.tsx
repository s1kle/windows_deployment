import Package from "../widgets/Package";
import "./MainPage.css";

const MainPage = () => {
  return (
    <>
      <div className="container packages">
        <h2 className="label">Packages</h2>
        <div className="wrapper">
          <Package />
        </div>
      </div>
      <div className="container states">
        <h2>States</h2>
      </div>
    </>
  );
};

export default MainPage;
