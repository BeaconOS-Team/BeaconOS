function module_check() 
{
    if python3 -m maskpass gnureadline; then
        ...
    else
        echo "Loader: Missing essencial modules...."
        exit 1
    fi
}

function installer() 
{
    if python3 -m pip; then
        if python3 -m pip install pkg/pkg_whl/maskpass-0.3.6-py3-none-any.whl pkg/pkg_whl/gnureadline-8.1.2-cp310-cp310-none_any.whl; then
            echo '\n'
            echo "Loader: Successfully installed modules needed"
        else
            echo "Loader: Installation failed"
            exit 1
        fi
    else
        if python3 $pwd/pkg/pip-22.2.2/setup.py install; then
            echo "Loader: successfullu installed pip"
        fi
    fi
}
while true
do
    if installer; then
        break
    else
        echo "Loader: Installation failed"
    fi
done
python3 login_assets.py