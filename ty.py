import dash
import dash_core_components as dcc
import dash_html_components as html
app=dash.Dash(__name__)

app.layout= html.Div(children=[html.H1('Hello Dashboard'),
html.Div("This is the sub heading"),
dcc.Graph(
id="Graph-a",
figure={
    'data':[
        {
            'x': [1,2,3], 'y':[2,5,6],'type':'bar','name':'bar 1'
        },
        {
            'x': [1,2,3], 'y':[4,2,1],'type':'bar','name':'bar 2'

        }],
     'layout': {
        'title':'Dash Visulization'
    }
}),
dcc.Graph(
id="Graph-ac",
figure={
    'data':[
        {
            'x': [1,2,3], 'y':[2,5,6],'type':'bar','name':'bar 1'
        },
        {
            'x': [1,2,3], 'y':[4,2,1],'type':'bar','name':'bar 2'

        }],
     'layout': {
        'title':'Dash Visulization'
    }
})])
if __name__ == '__main__':
    app.run_server(debug=True)
