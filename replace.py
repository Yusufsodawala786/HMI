import re
counter = 0
text = """
import React from "react";

const Color1 = () => {
  return (
    <svg
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      xmlnsXlink="http://www.w3.org/1999/xlink"
      x="0px"
      y="0px"
      viewBox="0 0 500 500"
      style={{ enableBackground: "new 0 0 500 500" }}
      xmlSpace="preserve"
    >
      <g id="BACKGROUND">
        <rect style={{ fill: "#FFFFFF" }} width={500} height={500} />
      </g>
      <g id="OBJECTS">
        <g>
          <defs>
            <rect id="SVGID_1_" width={500} height={500} />
          </defs>
          <clipPath id="SVGID_00000092436216046732507620000014680356467201357960_">
            <use xlinkHref="#SVGID_1_" style={{ overflow: "visible" }} />
          </clipPath>
          <rect
            x="-7.484"
            y="462.655"
            style={{
              clipPath:
                "url(#SVGID_00000092436216046732507620000014680356467201357960_)",
              fill: "#FFFFFF",
              stroke: "#231F20",
              strokeWidth: 2,
              strokeLinecap: "round",
              strokeLinejoin: "round",
              strokeMiterlimit: 10,
            }}
            width="514.702"
            height="50.164"
          />
        </g>
        <g>
          <g>
            <path
                fill={props.fillColor[0]}
                onClick={()=>{props.onFill(0)}}
              style={{
                fill: "#FFFFFF",
                stroke: "#231F20",
                strokeLinecap: "round",
                strokeLinejoin: "round",
                strokeMiterlimit: 10,
              }}
              d="M235.986,44.666
				c0.443,0.16,0.886,0.321,1.329,0.481c-5.867-4.053-13.181-5.964-20.281-5.299c-7.1,0.665-13.571,3.169-18.583,8.242
				c-4.694-13.735-17.82-24.184-32.258-25.679c14.508-3.817,29.517,1.349,39.069,12.916c5.578-2.366,12.644-3.174,18.468-1.503
				C229.555,35.496,232.512,39.701,235.986,44.666z"
            />
            <path
                fill={props.fillColor[1]}
                onClick={()=>{props.onFill(1)}}
              style={{
                fill: "#FFFFFF",
                stroke: "#231F20",
                strokeLinecap: "round",
                strokeLinejoin: "round",
                strokeMiterlimit: 10,
              }}
              d="
				M477.769,178.732c3.217-11.099,11.257-21.606,20.631-28.363c-11.101-1.138-23.074,5.329-28.114,15.286
				c-4.114-6.544-11.011-11.273-18.599-12.75c-7.587-1.477-15.755,0.318-22.023,4.841
				C447.276,157.224,465.841,165.763,477.769,178.732z"
            />
          </g>
          <g>
            <g>
              <g>
                <path
                    fill={props.fillColor[2]}
                    onClick={()=>{props.onFill(2)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeWidth: 2,
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M81.171,10.659c0,21.742-25.545,31.039-39.954,14.542c14.41,16.497,0.818,40.039-21.259,36.822
						c22.077,3.217,26.797,29.988,7.383,41.873c19.414-11.885,40.238,5.589,32.571,27.33c7.667-21.742,34.851-21.742,42.519,0
						c-7.667-21.742,13.157-39.215,32.571-27.33c-19.414-11.885-14.694-38.656,7.383-41.873
						c-22.077,3.217-35.669-20.325-21.259-36.822C106.715,41.698,81.171,32.4,81.171,10.659z"
                />
              </g>
              <ellipse
                transform="matrix(0.7071 -0.7071 0.7071 0.7071 -26.657 78.2857)"
                style={{
                  fill: "#FFFFFF",
                  stroke: "#231F20",
                  strokeWidth: 2,
                  strokeLinecap: "round",
                  strokeLinejoin: "round",
                  strokeMiterlimit: 10,
                }}
                cx="81.171"
                cy="71.321"
                rx="29.858"
                ry="29.858"
              />
            </g>
            <g>
              <path
                fill={props.fillColor[3]}
                onClick={()=>{props.onFill(3)}}
                style={{
                  fill: "none",
                  stroke: "#231F20",
                  strokeWidth: 2,
                  strokeLinecap: "round",
                  strokeLinejoin: "round",
                  strokeMiterlimit: 10,
                }}
                d="
					M74.134,85.625c2.958,2.257,6.772,3.165,10.335,2.46c3.563-0.705,6.83-3.015,8.853-6.258"
              />
              <path
                fill={props.fillColor[4]}
                onClick={()=>{props.onFill(4)}}
                style={{
                  fill: "none",
                  stroke: "#231F20",
                  strokeWidth: 2,
                  strokeLinecap: "round",
                  strokeLinejoin: "round",
                  strokeMiterlimit: 10,
                }}
                d="
					M66.375,83.226c0.707-2.15,2.317-3.932,4.291-4.751c1.974-0.818,4.275-0.658,6.135,0.427"
              />
              <path
                fill={props.fillColor[5]}
                onClick={()=>{props.onFill(5)}}
                style={{
                  fill: "none",
                  stroke: "#231F20",
                  strokeWidth: 2,
                  strokeLinecap: "round",
                  strokeLinejoin: "round",
                  strokeMiterlimit: 10,
                }}
                d="
					M87.263,76.016c1.444-1.558,3.372-2.586,5.396-2.878c2.025-0.291,4.134,0.155,5.907,1.251"
              />
            </g>
          </g>
        </g>
        <g>
          <defs>
            <rect
              id="SVGID_00000064348284825940010650000016424381971051117449_"
              width={500}
              height={500}
            />
          </defs>
          <clipPath id="SVGID_00000100345905126052580490000002842594080290187905_">
            <use
              xlinkHref="#SVGID_00000064348284825940010650000016424381971051117449_"
              style={{ overflow: "visible" }}
            />
          </clipPath>
          <g
            style={{
              clipPath:
                "url(#SVGID_00000100345905126052580490000002842594080290187905_)",
            }}
          >
            <g>
              <g>
                <path
                    fill={props.fillColor[6]}
                    onClick={()=>{props.onFill(6)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeWidth: 2,
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M-33.752,358.117h31.29c0-90.717,73.531-164.249,164.249-164.249v-31.29C53.798,162.578-33.752,250.128-33.752,358.117z"
                />
                <path
                    fill={props.fillColor[7]}
                    onClick={()=>{props.onFill(7)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeWidth: 2,
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M-2.462,358.117h31.177c0-73.503,59.569-133.072,133.072-133.072v-31.177C71.069,193.868-2.462,267.4-2.462,358.117z"
                />
                <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeWidth: 2,
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M28.715,358.117h30.339c0-56.743,45.991-102.734,102.734-102.734v-30.339C88.284,225.045,28.715,284.614,28.715,358.117z"
                />
              </g>
              <path
                fill={props.fillColor[0]}
                onClick={()=>{props.onFill(0)}}
                style={{
                  fill: "#FFFFFF",
                  stroke: "#231F20",
                  strokeWidth: 2,
                  strokeLinecap: "round",
                  strokeLinejoin: "round",
                  strokeMiterlimit: 10,
                }}
                d="
					M-4.484,312.695c7.15-0.505,14.469,1.744,20.004,6.148c5.535,4.404,9.226,10.914,10.087,17.794
					c8.304-9.285,21.942-12.708,33.453-7.529c11.512,5.179,18.655,18.176,16.653,30.296c6.612-1.375,13.058,0.326,17.928,4.862
					s7.206,11.478,6.029,17.916c9.44-4.779,20.225-4.205,29.543,0.794c9.318,4.999,15.747,14.705,16.546,24.977H-4.484V312.695z"
              />
            </g>
            <g>
              <g>
                <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeWidth: 2,
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M306.591,145.059v25.884c75.044,0,135.871,60.827,135.871,135.871h25.884C468.346,217.482,395.922,145.059,306.591,145.059z"
                />
                <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeWidth: 2,
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M306.591,170.943v25.79c60.803,0,110.081,49.277,110.081,110.081h25.79C442.462,231.77,381.635,170.943,306.591,170.943z"
                />
                <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeWidth: 2,
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M306.591,196.733v25.097c46.939,0,84.984,38.045,84.984,84.984h25.097C416.672,246.01,367.395,196.733,306.591,196.733z"
                />
              </g>
              <path
                fill={props.fillColor[0]}
                onClick={()=>{props.onFill(0)}}
                style={{
                  fill: "#FFFFFF",
                  stroke: "#231F20",
                  strokeWidth: 2,
                  strokeLinecap: "round",
                  strokeLinejoin: "round",
                  strokeMiterlimit: 10,
                }}
                d="
					M505.955,266.217c-4.434-15.43-21.156-26.268-37.051-24.016c-15.896,2.253-28.947,17.31-28.919,33.365
					c-7.543-5.716-18.484-5.72-25.811,0.27c-7.327,5.99-9.813,17.178-5.711,25.706c-8.864-6.28-23.311-4.692-31.524,2.419
					c-8.213,7.111-10.724,20.012-5.777,29.684c-7.988-3.127-19.181-2.293-26.221,2.609c-7.04,4.902-11.396,13.437-11.234,22.014
					h172.249V266.217z"
              />
            </g>
            <g>
              <g>
                <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeWidth: 2,
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M338.951-85.219v25.884c75.044,0,135.871,75.827,135.871,150.871h25.884C500.705,2.205,428.282-85.219,338.951-85.219z"
                />
                <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeWidth: 2,
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M338.951-59.335v25.79c60.803,0,110.081,64.277,110.081,125.081h25.79C474.822,16.492,413.995-59.335,338.951-59.335z"
                />
                <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeWidth: 2,
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M338.951-33.545v25.097c46.939,0,84.984,53.045,84.984,99.984h25.097C449.031,30.733,399.754-33.545,338.951-33.545z"
                />
              </g>
              <path
                fill={props.fillColor[0]}
                onClick={()=>{props.onFill(0)}}
                style={{
                  fill: "#FFFFFF",
                  stroke: "#231F20",
                  strokeWidth: 2,
                  strokeLinecap: "round",
                  strokeLinejoin: "round",
                  strokeMiterlimit: 10,
                }}
                d="
					M507.218,63.542c-3.209-6.939-10.96-11.495-18.584-10.922c-7.624,0.573-14.608,6.235-16.744,13.576
					c-1.438-8.796-10.929-15.821-19.841-15.666c-8.911,0.155-17.147,6.608-20.209,14.978c-3.062,8.37-1.203,18.153,4.037,25.362
					c-8.394-2.06-19.547,1.42-25.972,7.202c-6.425,5.782-9.742,14.832-8.576,23.396h105.888V63.542z"
              />
            </g>
          </g>
        </g>
        <g>
          <path
            fill={props.fillColor[0]}
            onClick={()=>{props.onFill(0)}}
            style={{
              fill: "#FFFFFF",
              stroke: "#231F20",
              strokeWidth: 2,
              strokeLinecap: "round",
              strokeLinejoin: "round",
              strokeMiterlimit: 10,
            }}
            d="
			M167.252,468.963c-0.112,0-87.59,0-87.59,0c-5.368-12.782-16.33-22.759-29.125-28.094c16.932-1.604,34.366,2.678,48.628,11.945
			c-6.025-19.762-19.864-37.025-37.842-47.205c23.966,1.387,47.033,14.098,61.006,33.618c-4.377-16.564-1.576-34.894,7.547-49.395
			c0.504,15.578,4.433,31.037,11.43,44.965c7.355-13.068,19.967-23.076,34.364-27.269c-6.382,9.374-9.749,20.565-10.811,31.788
			C164.614,441.901,163.741,468.963,167.252,468.963z"
          />
          <path
            fill={props.fillColor[0]}
            onClick={()=>{props.onFill(0)}}
            style={{
              fill: "#FFFFFF",
              stroke: "#231F20",
              strokeWidth: 2,
              strokeLinecap: "round",
              strokeLinejoin: "round",
              strokeMiterlimit: 10,
            }}
            d="
			M442.462,468.963H313.27c4.261-11.449,3.492-23.472,0.126-35.215c-3.366-11.743-10.575-22.351-20.254-29.804
			c17.961,3.741,33.882,15.597,44.049,30.868c-3.283-23.67-12.512-46.203-26.475-65.595c26.98,7.963,49.012,30.88,55.906,58.153
			c1.743-14.733,6.626-29.667,15.348-41.668c-2.626,14.141-0.77,29.079,5.235,42.148c10.572-16.2,26.888-27.69,46.033-30.462
			c-13.506,9.476-20.655,27.22-17.491,43.412c12.974-8.953,25.041-16.267,40.234-20.465
			C442.88,431.674,436.657,452.638,442.462,468.963z"
          />
          <g>
            <g>
              <g>
                <g>
                  <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                    style={{
                      fill: "#FFFFFF",
                      stroke: "#231F20",
                      strokeWidth: 2,
                      strokeLinecap: "round",
                      strokeLinejoin: "round",
                      strokeMiterlimit: 10,
                    }}
                    d="
							M286.538,303.957c9.301,9.984,23.035,14.598,37.453,12.583c14.417-2.015,29.352-10.636,40.726-23.509
							c-9.413-9.331-22.171-13.973-36.196-12.427C314.496,282.151,298.332,292.288,286.538,303.957z"
                  />
                  <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                    style={{
                      fill: "none",
                      stroke: "#231F20",
                      strokeWidth: 2,
                      strokeLinecap: "round",
                      strokeLinejoin: "round",
                      strokeMiterlimit: 10,
                    }}
                    d="
							M349.282,295.08c-17.061-1.163-38.2,2.035-62.744,8.877"
                  />
                </g>
                <g>
                  <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                    style={{
                      fill: "#FFFFFF",
                      stroke: "#231F20",
                      strokeWidth: 2,
                      strokeLinecap: "round",
                      strokeLinejoin: "round",
                      strokeMiterlimit: 10,
                    }}
                    d="
							M281.979,340.966c-15.623,0.255-31.158-6.002-42.363-17.061c-11.205-11.06-17.951-26.796-18.395-42.91
							c15.236,0.249,29.931,5.827,41.139,16.314C273.568,307.796,280.269,325.356,281.979,340.966z"
                  />
                  <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                    style={{
                      fill: "none",
                      stroke: "#231F20",
                      strokeWidth: 2,
                      strokeLinecap: "round",
                      strokeLinejoin: "round",
                      strokeMiterlimit: 10,
                    }}
                    d="
							M233.297,292.764c15.898,10.764,32.145,27.14,48.682,48.202"
                  />
                </g>
                <g>
                  <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                    style={{
                      fill: "#FFFFFF",
                      stroke: "#231F20",
                      strokeWidth: 2,
                      strokeMiterlimit: 10,
                    }}
                    d="M256.715,471.685
							c-0.371,0-0.746-0.031-1.124-0.098c-3.536-0.616-5.904-3.982-5.287-7.52l46.268-265.436c0.617-3.537,3.988-5.902,7.52-5.287
							c3.536,0.616,5.903,3.983,5.287,7.52L263.11,466.3C262.56,469.459,259.814,471.685,256.715,471.685z"
                  />
                </g>
              </g>
              <g>
                <g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M385.101,110.083c-11.763,12.917-33.557,4.448-33.557,4.448s-10.465-20.909,1.298-33.826
									c11.763-12.917,41.3-12.951,41.3-12.951S396.864,97.166,385.101,110.083z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="381.717"
                        y1="81.398"
                        x2="351.544"
                        y2="114.531"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M290.32,214.533c11.763-12.917,1.298-33.826,1.298-33.826s-21.794-8.469-33.557,4.448
									c-11.763,12.917-9.041,42.328-9.041,42.328S278.557,227.449,290.32,214.533z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="261.445"
                        y1="213.839"
                        x2="291.618"
                        y2="180.707"
                      />
                    </g>
                  </g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M303.844,219.237c-0.971-17.443,20.343-27.056,20.343-27.056s22.25,7.187,23.221,24.63
									c0.971,17.443-19.704,38.538-19.704,38.538S304.816,236.681,303.844,219.237z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="326.679"
                        y1="236.924"
                        x2="324.188"
                        y2="192.182"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M295.753,78.426c0.971,17.443,23.221,24.63,23.221,24.63S340.289,93.444,339.318,76
									c-0.971-17.443-23.86-36.112-23.86-36.112S294.782,60.983,295.753,78.426z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="316.483"
                        y1="58.313"
                        x2="318.974"
                        y2="103.056"
                      />
                    </g>
                  </g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M358.766,211.345c-12.852-11.834-4.263-33.581-4.263-33.581s20.966-10.35,33.818,1.484
									c12.852,11.834,12.722,41.371,12.722,41.371S371.618,223.18,358.766,211.345z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="387.468"
                        y1="208.119"
                        x2="354.503"
                        y2="177.764"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M254.841,115.989c12.852,11.834,33.818,1.484,33.818,1.484s8.589-21.747-4.263-33.581
									c-12.852-11.834-42.278-9.274-42.278-9.274S241.989,104.155,254.841,115.989z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="255.694"
                        y1="87.118"
                        x2="288.659"
                        y2="117.473"
                      />
                    </g>
                  </g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M250.054,129.516c17.448-0.882,26.951,20.481,26.951,20.481s-7.3,22.213-24.748,23.095
									c-17.448,0.882-38.437-19.901-38.437-19.901S232.606,130.398,250.054,129.516z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="232.251"
                        y1="152.26"
                        x2="277.005"
                        y2="149.997"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M390.905,122.146c-17.448,0.882-24.749,23.095-24.749,23.095s9.503,21.363,26.951,20.481
									c17.448-0.882,36.234-23.675,36.234-23.675S408.353,121.264,390.905,122.146z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="410.911"
                        y1="142.978"
                        x2="366.156"
                        y2="145.24"
                      />
                    </g>
                  </g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M248.498,157.754c15.835-7.381,32.676,8.838,32.676,8.838s1.592,23.327-14.242,30.708c-15.835,7.381-43.1-3.979-43.1-3.979
									S232.664,165.135,248.498,157.754z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="240.558"
                        y1="185.524"
                        x2="281.175"
                        y2="166.592"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M376.23,97.938c-15.834,7.381-14.242,30.708-14.242,30.708s16.842,16.219,32.676,8.838
									c15.835-7.381,24.666-35.567,24.666-35.567S392.064,90.557,376.23,97.938z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="402.603"
                        y1="109.713"
                        x2="361.987"
                        y2="128.646"
                      />
                    </g>
                  </g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M331.716,220.702c-7.381-15.835,8.838-32.676,8.838-32.676s23.327-1.592,30.708,14.242c7.381,15.835-3.979,43.1-3.979,43.1
									S339.097,236.536,331.716,220.702z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="359.486"
                        y1="228.641"
                        x2="340.554"
                        y2="188.025"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M271.9,92.97c7.381,15.835,30.708,14.243,30.708,14.243s16.219-16.842,8.838-32.676
									c-7.381-15.835-35.567-24.666-35.567-24.666S264.519,77.135,271.9,92.97z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="283.676"
                        y1="66.596"
                        x2="302.608"
                        y2="107.213"
                      />
                    </g>
                  </g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M380.425,192.13c-16.416-5.977-16.856-29.355-16.856-29.355s15.369-17.621,31.785-11.643
									c16.416,5.978,27.662,33.29,27.662,33.29S396.841,198.107,380.425,192.13z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="405.676"
                        y1="178.107"
                        x2="363.568"
                        y2="162.775"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M247.809,144.106c16.416,5.977,31.785-11.643,31.785-11.643s-0.44-23.377-16.856-29.355
									c-16.416-5.978-42.591,7.708-42.591,7.708S231.393,138.129,247.809,144.106z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="237.486"
                        y1="117.13"
                        x2="279.594"
                        y2="132.463"
                      />
                    </g>
                  </g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M366.092,88.775c-5.978,16.416-29.355,16.856-29.355,16.856s-17.621-15.369-11.643-31.785
									c5.978-16.416,33.29-27.662,33.29-27.662S372.069,72.359,366.092,88.775z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="352.069"
                        y1="63.524"
                        x2="336.737"
                        y2="105.632"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M318.068,221.391c5.978-16.416-11.643-31.785-11.643-31.785s-23.378,0.441-29.355,16.856s7.708,42.591,7.708,42.591
									S312.091,237.807,318.068,221.391z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="291.093"
                        y1="231.714"
                        x2="306.425"
                        y2="189.606"
                      />
                    </g>
                  </g>
                </g>
                <g>
                  <ellipse
                    transform="matrix(0.9669 -0.2553 0.2553 0.9669 -27.0312 86.9954)"
                    style={{
                      fill: "#FFFFFF",
                      stroke: "#231F20",
                      strokeWidth: 2,
                      strokeLinecap: "round",
                      strokeLinejoin: "round",
                      strokeMiterlimit: 10,
                    }}
                    cx="321.581"
                    cy="147.619"
                    rx="60.83"
                    ry="60.831"
                  />
                  <g>
                    <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                      style={{ fill: "#231F20" }}
                      d="M299.426,144.024c-1.292,2.566-4.42,3.598-6.986,2.306c-2.566-1.292-3.598-4.42-2.306-6.986
								c1.292-2.566,4.42-3.598,6.986-2.306C299.686,138.331,300.718,141.459,299.426,144.024z"
                    />
                    <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                      style={{ fill: "#231F20" }}
                      d="M353.092,154.984c-1.292,2.566-4.42,3.598-6.986,2.306c-2.566-1.292-3.598-4.42-2.306-6.986
								c1.292-2.566,4.42-3.598,6.986-2.306C353.352,149.29,354.385,152.418,353.092,154.984z"
                    />
                    <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                      style={{
                        fill: "none",
                        stroke: "#231F20",
                        strokeWidth: 2,
                        strokeLinecap: "round",
                        strokeLinejoin: "round",
                        strokeMiterlimit: 10,
                      }}
                      d="
								M299.479,154.29c3.844,6.5,10.382,11.35,17.718,13.143c7.336,1.793,15.374,0.506,21.783-3.488"
                    />
                  </g>
                </g>
              </g>
            </g>
            <g>
              <g>
                <g>
                  <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                    style={{
                      fill: "#FFFFFF",
                      stroke: "#231F20",
                      strokeWidth: 2,
                      strokeLinecap: "round",
                      strokeLinejoin: "round",
                      strokeMiterlimit: 10,
                    }}
                    d="
							M209.922,366.261c-9.838,6.718-22.331,9.427-34.068,7.387c-11.737-2.04-22.583-8.807-29.576-18.451
							c9.801-6.249,21.477-9.019,32.978-7.328C190.757,349.559,202.333,357.457,209.922,366.261z"
                  />
                  <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                    style={{
                      fill: "none",
                      stroke: "#231F20",
                      strokeWidth: 2,
                      strokeLinecap: "round",
                      strokeLinejoin: "round",
                      strokeMiterlimit: 10,
                    }}
                    d="
							M158.865,357.305c14.601-0.112,31.761,3.054,51.057,8.957"
                  />
                </g>
                <g>
                  <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                    style={{
                      fill: "#FFFFFF",
                      stroke: "#231F20",
                      strokeWidth: 2,
                      strokeLinecap: "round",
                      strokeLinejoin: "round",
                      strokeMiterlimit: 10,
                    }}
                    d="
							M215.153,387.801c10.686,0.174,21.313-4.105,28.977-11.67c7.664-7.565,12.279-18.329,12.583-29.352
							c-10.422,0.17-20.474,3.986-28.14,11.159C220.907,365.111,216.323,377.123,215.153,387.801z"
                  />
                  <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                    style={{
                      fill: "none",
                      stroke: "#231F20",
                      strokeWidth: 2,
                      strokeLinecap: "round",
                      strokeLinejoin: "round",
                      strokeMiterlimit: 10,
                    }}
                    d="
							M248.453,354.829c-10.875,7.363-21.988,18.564-33.3,32.972"
                  />
                </g>
                <g>
                  <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                    style={{
                      fill: "#FFFFFF",
                      stroke: "#231F20",
                      strokeWidth: 2,
                      strokeMiterlimit: 10,
                    }}
                    d="M233.414,462.655
							c-2.952,0-5.624-2.023-6.324-5.022c-16.848-72.129-37.728-144.173-62.061-214.132c-1.179-3.391,0.613-7.095,4.004-8.274
							c3.391-1.18,7.095,0.614,8.274,4.004c24.482,70.388,45.49,142.874,62.441,215.446c0.816,3.496-1.355,6.991-4.851,7.809
							C234.401,462.6,233.903,462.655,233.414,462.655z"
                  />
                </g>
              </g>
              <g>
                <g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M218.765,168.2c-6.633,16.162-30.01,15.661-30.01,15.661s-16.988-16.066-10.354-32.228s34.376-26.3,34.376-26.3
									S225.399,152.038,218.765,168.2z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="205.771"
                        y1="142.405"
                        x2="188.755"
                        y2="183.861"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M165.442,298.776c6.633-16.162-10.354-32.228-10.354-32.228s-23.376-0.501-30.01,15.661
									c-6.634,16.162,5.988,42.867,5.988,42.867S158.809,314.938,165.442,298.776z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="138.073"
                        y1="308.004"
                        x2="155.088"
                        y2="266.547"
                      />
                    </g>
                  </g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M179.76,298.569c-6.881-16.058,9.858-32.383,9.858-32.383s23.366-0.86,30.247,15.198
									c6.881,16.058-5.329,42.954-5.329,42.954S186.641,314.627,179.76,298.569z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="207.268"
                        y1="307.375"
                        x2="189.618"
                        y2="266.186"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M123.979,169.025c6.881,16.058,30.247,15.198,30.247,15.198s16.739-16.325,9.858-32.383
									c-6.881-16.058-34.776-25.769-34.776-25.769S117.098,152.967,123.979,169.025z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="136.575"
                        y1="143.033"
                        x2="154.225"
                        y2="184.223"
                      />
                    </g>
                  </g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M228.666,272.362c-16.125-6.723-15.495-30.096-15.495-30.096s16.159-16.899,32.285-10.176
									c16.125,6.723,26.11,34.521,26.11,34.521S244.792,279.084,228.666,272.362z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="254.533"
                        y1="259.51"
                        x2="213.171"
                        y2="242.266"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M98.387,218.319c16.125,6.723,32.285-10.176,32.285-10.176s0.63-23.373-15.495-30.096
									c-16.125-6.723-42.899,5.751-42.899,5.751S82.262,211.596,98.387,218.319z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="89.311"
                        y1="190.899"
                        x2="130.672"
                        y2="208.143"
                      />
                    </g>
                  </g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M98.518,232.667c16.093-6.799,32.332,10.024,32.332,10.024s0.74,23.37-15.353,30.169s-42.926-5.548-42.926-5.548
									S82.425,239.466,98.518,232.667z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="89.571"
                        y1="260.13"
                        x2="130.85"
                        y2="242.691"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M228.346,177.549c-16.093,6.799-15.353,30.169-15.353,30.169s16.239,16.822,32.332,10.024
									c16.093-6.799,25.946-34.644,25.946-34.644S244.439,170.751,228.346,177.549z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="254.273"
                        y1="190.279"
                        x2="212.993"
                        y2="207.718"
                      />
                    </g>
                  </g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M106.718,259.733c12.353-12.354,33.728-2.876,33.728-2.876s9.477,21.375-2.876,33.728
									c-12.353,12.353-41.86,11.008-41.86,11.008S94.364,272.086,106.718,259.733z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="108.759"
                        y1="288.544"
                        x2="140.446"
                        y2="256.857"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M206.274,159.824c-12.353,12.354-2.876,33.728-2.876,33.728s21.375,9.478,33.728-2.876
									c12.353-12.353,11.008-41.86,11.008-41.86S218.627,147.47,206.274,159.824z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="235.085"
                        y1="161.865"
                        x2="203.398"
                        y2="193.552"
                      />
                    </g>
                  </g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M206.45,290.408c-12.354-12.353-2.876-33.728-2.876-33.728s21.375-9.477,33.728,2.876
									c12.353,12.353,11.008,41.86,11.008,41.86S218.804,302.762,206.45,290.408z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="235.261"
                        y1="288.367"
                        x2="203.574"
                        y2="256.68"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M106.541,190.852c12.354,12.353,33.728,2.876,33.728,2.876s9.478-21.375-2.876-33.728
									c-12.353-12.353-41.86-11.008-41.86-11.008S94.188,178.499,106.541,190.852z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="108.582"
                        y1="162.042"
                        x2="140.269"
                        y2="193.728"
                      />
                    </g>
                  </g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M242.443,246.895c-17.47,0-25.883-21.816-25.883-21.816s8.413-21.816,25.883-21.816s37.383,21.816,37.383,21.816
									S259.914,246.895,242.443,246.895z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="261.373"
                        y1="225.079"
                        x2="216.561"
                        y2="225.079"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M101.4,247.145c17.47,0,25.883-21.816,25.883-21.816s-8.412-21.816-25.883-21.816c-17.47,0-37.383,21.816-37.383,21.816
									S83.93,247.145,101.4,247.145z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="82.471"
                        y1="225.329"
                        x2="127.283"
                        y2="225.329"
                      />
                    </g>
                  </g>
                  <g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M193.613,154.683c0,17.47-21.816,25.883-21.816,25.883s-21.816-8.412-21.816-25.883s21.816-37.383,21.816-37.383
									S193.613,137.212,193.613,154.683z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="171.797"
                        y1="135.753"
                        x2="171.797"
                        y2="180.566"
                      />
                    </g>
                    <g>
                      <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                        style={{
                          fill: "#FFFFFF",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        d="
									M193.863,295.726c0-17.47-21.816-25.883-21.816-25.883s-21.816,8.413-21.816,25.883s21.816,37.383,21.816,37.383
									S193.863,313.196,193.863,295.726z"
                      />
                      <line
                        style={{
                          fill: "none",
                          stroke: "#231F20",
                          strokeWidth: 2,
                          strokeLinecap: "round",
                          strokeLinejoin: "round",
                          strokeMiterlimit: 10,
                        }}
                        x1="172.047"
                        y1="314.655"
                        x2="172.047"
                        y2="269.843"
                      />
                    </g>
                  </g>
                </g>
                <g>
                  <ellipse
                    transform="matrix(0.7071 -0.7071 0.7071 0.7071 -108.8888 187.5279)"
                    style={{
                      fill: "#FFFFFF",
                      stroke: "#231F20",
                      strokeWidth: 2,
                      strokeLinecap: "round",
                      strokeLinejoin: "round",
                      strokeMiterlimit: 10,
                    }}
                    cx="171.922"
                    cy="225.204"
                    rx="60.831"
                    ry="60.831"
                  />
                  <g>
                    <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                      style={{ fill: "#231F20" }}
                      d="M149.874,229.407c-0.336,2.853-2.922,4.893-5.775,4.557c-2.853-0.336-4.893-2.922-4.557-5.775
								c0.336-2.853,2.922-4.893,5.775-4.557C148.17,223.969,150.21,226.554,149.874,229.407z"
                    />
                    <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                      style={{ fill: "#231F20" }}
                      d="M204.051,221.343c-0.336,2.853-2.922,4.893-5.775,4.557c-2.853-0.336-4.893-2.922-4.557-5.775
								c0.336-2.853,2.922-4.893,5.775-4.557C202.347,215.904,204.387,218.49,204.051,221.343z"
                    />
                    <path
                        fill={props.fillColor[0]}
                        onClick={()=>{props.onFill(0)}}
                      style={{
                        fill: "none",
                        stroke: "#231F20",
                        strokeWidth: 2,
                        strokeLinecap: "round",
                        strokeLinejoin: "round",
                        strokeMiterlimit: 10,
                      }}
                      d="
								M153.436,239.036c5.836,4.793,13.639,7.113,21.146,6.288c7.507-0.825,14.619-4.785,19.275-10.731"
                    />
                  </g>
                </g>
              </g>
            </g>
            <g>
              <path
                fill={props.fillColor[0]}
                onClick={()=>{props.onFill(0)}}
                style={{
                  fill: "#FFFFFF",
                  stroke: "#231F20",
                  strokeWidth: 2,
                  strokeLinecap: "round",
                  strokeLinejoin: "round",
                  strokeMiterlimit: 10,
                }}
                d="
					M324.188,474.961H143.743c-6.765-4.728-10.104-12.974-8.565-21.083c1.539-8.109,7.243-15.099,14.421-19.171
					c7.179-4.072,15.689-5.411,23.922-4.832c-2.009-9.658-0.014-21.303,7.05-28.188c7.064-6.885,17.731-9.847,27.334-7.59
					c9.603,2.257,17.833,9.66,21.091,18.971c6.745-5.566,13.956-9.759,22.664-10.566s17.902,1.868,24.098,8.04
					c6.196,6.172,8.888,15.963,5.752,24.126c10.329-8.411,24.452-6.507,34.63,2.085
					C326.321,445.347,330.745,463.367,324.188,474.961z"
              />
              <g>
                <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M169.146,453.36c1.929,2.567,5.189,3.974,8.4,3.969c3.211-0.006,6.341-1.328,8.834-3.351c2.78-2.257,4.91-5.727,4.418-9.273
						C188.826,430.482,159.655,440.729,169.146,453.36z"
                />
                <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M192.09,419.801c-1.387,2.795-1.112,6.444,0.984,8.755c1.742,1.923,4.498,2.73,7.082,2.498c2.584-0.233,5.009-1.402,7.122-2.91
						c1.447-1.033,2.799-2.26,3.677-3.806s1.235-3.453,0.656-5.134c-1.427-4.146-6.789-4.703-10.515-4.911
						C197.444,414.089,193.707,416.543,192.09,419.801z"
                />
                <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M207.356,443.384c0.687,0.886,1.829,1.331,2.949,1.389c1.119,0.058,2.228-0.228,3.292-0.578
						c1.969-0.648,4.035-1.905,3.74-4.293c-0.219-1.778-1.899-3.613-3.683-3.897C210.298,435.469,204.609,439.841,207.356,443.384z"
                />
                <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M229.175,422.32c-1.361,0.868-2.392,2.298-2.613,3.897c-0.221,1.599,0.441,3.33,1.773,4.241
						c1.834,1.254,4.36,0.745,6.338-0.268c1.358-0.696,2.64-1.639,3.425-2.948c0.785-1.309,0.995-3.031,0.252-4.364
						C236.684,419.892,231.498,420.838,229.175,422.32z"
                />
                <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M255.692,450.352c-0.836,1.064-1.02,2.601-0.459,3.832c0.561,1.231,1.842,2.101,3.193,2.169
						c1.152,0.058,2.27-0.424,3.229-1.063c1.086-0.722,2.1-1.819,2.065-3.123C263.621,448.435,257.625,447.89,255.692,450.352z"
                />
                <path
                    fill={props.fillColor[0]}
                    onClick={()=>{props.onFill(0)}}
                  style={{
                    fill: "#FFFFFF",
                    stroke: "#231F20",
                    strokeLinecap: "round",
                    strokeLinejoin: "round",
                    strokeMiterlimit: 10,
                  }}
                  d="
						M294.592,445.668c-1.188,2.589-0.196,5.98,2.199,7.522c1.805,1.162,4.079,1.27,6.223,1.179c1.894-0.08,3.827-0.3,5.53-1.132
						c1.703-0.832,3.154-2.379,3.432-4.253c0.332-2.236-1.094-4.467-3.032-5.631C305.087,441.037,296.775,440.907,294.592,445.668z"
                />
              </g>
            </g>
          </g>
        </g>
      </g>
    </svg>
  );
};

export default Color1;
"""

def replace_occurrences(text):
    counter = -1
    def replace_match_fillColor(match):
        nonlocal counter
        counter += 1
        return match.group(1) + '`${props.fillColor['+str(counter) + ']}`'
    def replace_match_onFill(match):
        nonlocal counter
        counter += 1
        return match.group(1) + str(counter) + ')'

    pattern1 = r'(fill:\s*")(#[A-Fa-f0-9]{6})(")'
    pattern2 = r'(props\.onFill\()\d+(\))'
    modified_text = re.sub(pattern1, replace_match_fillColor, text)
    counter = -1
    final_text = re.sub(pattern2,replace_match_onFill,modified_text)
    return final_text

# Example usage:
modified_text = replace_occurrences(text)
print(modified_text)