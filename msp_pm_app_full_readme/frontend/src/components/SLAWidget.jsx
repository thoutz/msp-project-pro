
import React from "react";
export default function SLAWidget({data}) {
  return <div>SLA: {data ? data.percent + "%" : "Loading..."}</div>;
}
