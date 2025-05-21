import { Graph as G6Graph, NodeEvent, EdgeEvent,  } from '@antv/g6';
import { useEffect, useRef } from 'react';
import { FlowGraph as GsFlowGraph, RCNode as GsRCNode } from '@ant-design/graphs';

//docs: https://g6.antv.vision/manual/getting-started/integration/react

// export interface GraphProps {
//   options: GraphOptions;
//   onRender?: (graph: G6Graph) => void;
//   onDestroy?: () => void;
// }

export const RCNode = GsRCNode;


function _graphRef(graphRef, containerRef, props) {
  const { options, onRender, onDestroy } = props;

  useEffect(() => {
    const graph = new G6Graph({ container: containerRef.current });
    graphRef.current = graph;

    return () => {
      const graph = graphRef.current;
      if (graph) {
        graph.destroy();
        onDestroy?.();
        graphRef.current = undefined;
      }
    };
  }, []);

  useEffect(() => {
    const container = containerRef.current;
    const graph = graphRef.current;

    if (!options || !container || !graph || graph.destroyed) return;

    graph.setOptions(options);
    graph
      .render()
      .then(() => onRender?.(graph))
      // eslint-disable-next-line no-console
      .catch((error) => console.debug(error));
  }, [options]);
}

function initGraph(onClick, onReady) {
  const myReady = (g) => {
    if (onClick) {
      g.on(NodeEvent.CLICK, onClick);
    }
    if (onReady) {
      onReady(g);
    }
    return g;
  };
  return myReady;
}


export const FlowGraph = ({onClick, onReady, ...props}) => {
  const myReady = initGraph(onClick, onReady);

  return <GsFlowGraph onReady={myReady} {...props} />;
};

