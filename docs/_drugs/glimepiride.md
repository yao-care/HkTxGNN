---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 417
evidence_level: L5
indication_count: 5
---

# Glimepiride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Glimepiride：從第 2 型糖尿病到僵人症候群（預測）

## 一句話總結

Glimepiride（格列美脲）是一種磺醯脲類（sulfonylurea）降血糖藥，原本用於治療第 2 型糖尿病。
TxGNN 模型預測它可能對**典型僵人症候群 (Classic Stiff Person Syndrome)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測分數。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第 2 型糖尿病 |
| 預測新適應症 | 典型僵人症候群 (Classic Stiff Person Syndrome) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 19 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知的藥理資訊，glimepiride 是磺醯脲類藥物，主要透過關閉胰臟 β 細胞的 K-ATP 通道，促進胰島素分泌來降低血糖。

僵人症候群是一種自體免疫性神經疾病，與 GABA 及甘胺酸（glycine）神經傳導異常有關，常見抗 GAD65 抗體，也常與第 1 型糖尿病並存。TxGNN 給出的高分，較可能來自知識圖譜中「糖尿病」與「GAD 相關」節點的共同鄰居，而非真正的治療作用。

整體而言，現有資料並未建立可信的機轉連結，glimepiride 並不預期能治療這個神經系統疾病，此預測很可能是知識圖譜的間接關聯所造成的假象。

**其他預測結果（同樣僅有模型分數，無任何試驗或文獻）：**

| 排名 | 預測疾病 | 分數 | 說明 |
|------|---------|------|------|
| 2 | 局限性僵硬肢症候群 (Focal stiff limb syndrome) | 99.75% | 屬僵人症候群譜系，與典型型分數相同，應為同一圖譜訊號 |
| 3 | Opsismodysplasia | 99.74% | 與 INPPL1 突變及胰島素/PI3K 訊號有間接概念關聯，但屬推測 |
| 4 | 硫胺素反應性功能異常症候群 | 99.73% | 因共有糖尿病表型而被關聯；標準治療為補充硫胺素 |
| 5 | 藥物誘發局部脂肪失養症 | 99.62% | 多與注射藥物（如胰島素）有關，口服的 glimepiride 預期無效 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

本藥在香港共有 19 張有效的單一成分許可證，皆為上市中。下表列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-42323 | AMARYL TAB 2MG | SANOFI HONG KONG LIMITED |
| HK-42325 | AMARYL TAB 4MG | SANOFI HONG KONG LIMITED |
| HK-62478 | LIMERAL TABLETS 4MG | TEVA PHARMACEUTICAL HONG KONG |
| HK-57874 | GLIMEPIRIDE SANDOZ TAB 4MG | SANDOZ HONG KONG LIMITED |
| HK-58694 | APO-GLIMEPIRIDE TAB 2MG | HIND WING CO LTD |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自模型知識圖譜，並非仿單內容）：腎臟疾病、肝臟疾病、膽囊疾病、充血性心衰竭、腦下垂體功能低下（含多種生長激素缺乏、低促性腺激素性性腺功能低下、Kallmann 症候群、Sheehan 症候群等）、胸腺疾病、骨質疏鬆（含停經後骨質疏鬆）、感染性疾病。
- **藥物交互作用**：資料庫共記錄 100 筆，以下為部分範例（皆為中度，除另註明）：
  - 升糖或影響血糖控制相關：Hydrocortisone、Ethinylestradiol、Epinephrine、Salbutamol、Formoterol、Phenylephrine、Pseudoephedrine、Hydrochlorothiazide、Acetazolamide
  - 其他：Acebutolol（β 阻斷劑）、Famotidine、Ranitidine、Ibuprofen、Ketorolac、Ethanol、Acitretin、Nitazoxanide、Albiglutide
  - 輕度：外用 Hydrocortisone、外用 Alclometasone

主要警語與禁忌症的仿單資料尚未取得，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何臨床試驗或文獻佐證（證據等級 L5）。
- 缺乏機轉連結，高分很可能是糖尿病與 GAD 相關節點造成的圖譜假象，磺醯脲類藥物不預期能治療這類神經疾病。

**若要推進需要：**
- 取得 glimepiride 的詳細作用機轉資料（MOA）。
- 取得香港仿單的警語與禁忌症，完成安全性初步篩選。
- 找到支持僵人症候群的前臨床或臨床證據（目前完全沒有）。
- 以文獻檢索確認是否有磺醯脲類在相關疾病的使用報告（如硫胺素反應性症候群），再重新評估各預測的優先順序。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

