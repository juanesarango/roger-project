import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import InputRange from 'react-input-range';
import 'react-input-range/lib/css/index.css';


class App extends Component {
  constructor(props) {
    super(props);
    const { sitters } = props;
    this.state = {
        sitters: sitters,
        value: { min: 0, max: 5 },
    }
  }

  render() {
    return (
        <div className="sitters-list">
            <div className="list-header">
                <h2>FIND YOUR SITTER</h2>
                <div className="slider">
                    <InputRange
                        maxValue={5}
                        minValue={0}
                        step={0.2}
                        value={this.state.value}
                        onChange={value => this.setState({ 
                            value: {
                                min: value.min.toFixed(2),
                                max: value.max.toFixed(2)
                            } 
                        })} />
                </div>
            </div>
            {this.state.sitters.length ? (
                <ul>
                {this.state.sitters.filter(sitter => {
                    return sitter.overall_rank >= this.state.value.min && sitter.overall_rank <= this.state.value.max
                }).slice(0, 10).map((sitter, index) => (
                    <li className="sitter" key={index}>
                        <img className="sitter-image" src={sitter.image} alt="Profile pic of sitter" />
                        <div className="sitter-profile">
                            <div className="sitter-name">{sitter.name}</div><br/>
                            <div className="sitter-rank">Overall Rank: {sitter.overall_rank.toFixed(2)}</div>
                            <RankScore score={ sitter.overall_rank }/>         
                        </div>
                    </li>
                ))}
                </ul>
            ) : (
                <p>No sitters are available.</p>
            )}
        </div>
    );
  }
}

class RankScore extends Component {
    render() {
        return (
            <div className="container">
                <svg width="30%" height="30%" viewBox="0 0 100 20" version="1.1">
                    <defs>
                        <pattern id="pattern1" x="0" y="0" width="20" height="20"
                                patternUnits="userSpaceOnUse" >     
                            <circle cx="10" cy="10" r="5" style={{fill:'white'}} />
                        </pattern>
                        <pattern id="pattern2" x="0" y="0" width="20" height="20"
                                patternUnits="userSpaceOnUse" >     
                            <circle cx="10" cy="10" r="9" style={{fill:'white'}} />
                            <circle cx="10" cy="10" r="7" style={{fill:'black'}} />
                            </pattern>
                        <mask id="mask1" x="0" y="0" width="100" height="20" >
                            <rect x="0" y="0"  width="100" height="20"
                                style={{stroke: 'none', fill: 'url(#pattern2)'}}/>
                        </mask>    
                        <mask id="mask2" x="0" y="0" width="100" height="20" >
                            <rect x="0" y="0"  width="100" height="20"
                                style={{stroke: 'none', fill: 'url(#pattern1)'}}/>
                        </mask>
                    </defs>
                    <rect x="0" y="0" width="500" height="20" fill="url(#pattern2)" style={{fill:'#FFC107', mask: 'url(#mask1)'}}/>
                    <rect x="0" y="0" width={ this.props.score*20 } height="20" style={{fill:'#FFC107', mask: 'url(#mask2)'}}/>
                </svg>
            </div>   
        )
    }
}

ReactDOM.render(<App sitters={ window._SITTERS_LIST }/>, 
    document.getElementById('filter-react-app')
)