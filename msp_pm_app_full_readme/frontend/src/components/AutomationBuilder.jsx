
import React from "react";
import ReactFlow from "react-flow-renderer";

export default function AutomationBuilder() {
  const elements = [
    { id: "1", type: "input", data: { label: "Trigger: SLA Breach" }, position: { x: 250, y: 0 } },
    { id: "2", data: { label: "Action: Notify Tech Lead" }, position: { x: 250, y: 100 } },
    { id: "e1-2", source: "1", target: "2", type: "smoothstep" }
  ];
  return <ReactFlow elements={elements} style={{ width: "100%", height: 300 }} />;
}
