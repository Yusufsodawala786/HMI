import React from "react";
import { Outlet, useNavigation } from "react-router-dom";
import { CircularProgress } from "@nextui-org/react";
import Navbar from "../components/UI/Navbar";

const RootLayout = () => {
  const navigation = useNavigation();
  return (
    <main className="flex flex-col min-h-screen">
      <Navbar />
      {navigation.state === "loading" ? (
        <div className="flex flex-col items-center h-screen bg-gray-200 w-full justify-center gap-3 sm:text-base">
          <span className="text-3xl">
            Have patience, we are loading your data...
          </span>
          <CircularProgress
            size="md"
            classNames={{
              svg: "w-24 h-24",
            }}
          />
        </div>
      ) : (
        <Outlet />
      )}
    </main>
  );
};

export default RootLayout;
