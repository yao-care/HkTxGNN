---
layout: default
title: Brodalumab
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Brodalumab：預測新適應症為類圓線蟲病 (Strongyloidiasis)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "Brodalumab"
predicted_indications: ["strongyloidiasis", "eye disease", "vitamin deficiency disorder", "von Hippel anomaly", "optic perineuritis", "recurrent idiopathic neuroretinitis", "chronic relapsing inflammatory optic neuropathy", "isolated optic neuritis", "nodular episcleritis", "episcleritis periodica fugax"]
---

# Brodalumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Brodalumab：從（原適應症未載明）到 Strongyloidiasis（類圓線蟲病）

## 一句話總結

Brodalumab 是一種 IL-17 受體 A (IL-17RA) 拮抗劑，在香港已取得許可證，但本報告編譯的資料中未載明其核准適應症。
TxGNN 模型預測它可能對 **類圓線蟲病 (Strongyloidiasis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明（香港許可證的核准適應症欄位為空白） |
| 預測新適應症 | 類圓線蟲病 (Strongyloidiasis) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Brodalumab 是 IL-17 受體 A 拮抗劑，可同時阻斷多種 IL-17 家族細胞激素的訊號傳遞。IL-17 路徑在宿主對部分病原體的防禦中有角色。

不過，類圓線蟲病是由蠕蟲引起的感染，免疫反應主要由 Th2／嗜酸性球驅動。阻斷 IL-17R 預期無法治療此病，甚至可能因免疫調節而削弱對寄生蟲的控制，使病情惡化。

因此，目前看不出明確的機轉連結。這個高分更像是知識圖譜的模型預測結果，缺乏任何實證支持。

其他排名較前的預測中，**眼部發炎性疾病**（如視神經炎、葡萄膜炎相關）在機轉上較有理論依據（IL-17／Th17 參與發炎），但同樣缺乏療效證據，且有潛在安全性訊號（見下文）。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對預測適應症「類圓線蟲病」，目前無相關文獻。

作為參考，排名第 2 的預測「眼部疾病 (eye disease)」有以下文獻，但**均未顯示療效**：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41770262](https://pubmed.ncbi.nlm.nih.gov/41770262/) | 2026 | 病例報告 | Rheumatology International | 慢性非細菌性骨炎患者在開始使用 brodalumab 後出現貝賽特氏症，為矛盾性反應 |
| [41916603](https://pubmed.ncbi.nlm.nih.gov/41916603/) | 2026 | 藥物警訊分析 | Canadian Journal of Ophthalmology | 分析全身性藥物與葡萄膜炎通報的關聯，屬安全性訊號而非療效 |
| [42576218](https://pubmed.ncbi.nlm.nih.gov/42576218/) | 2026 | 前臨床 | Journal of Translational Medicine | IL-17R 抑制可減輕實驗性牙周炎（非眼部疾病） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66126 | LUMICEF 預填充注射筒注射液 210mg/1.5ml（DKSH Hong Kong Limited） | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：克隆氏症 (Crohn disease)、發炎性腸道疾病 (IBD)、克隆氏結腸炎 (Crohn's colitis)。此資訊來自 TxGNN 知識圖譜的藥物－疾病關聯，並非仿單文字。
- **藥物交互作用**：共查得 68 筆，以下為主要項目：
  - **重大 (Major)**：Adalimumab、Baricitinib、Certolizumab pegol、卡介苗 (BCG) 活菌疫苗
  - **中度 (Moderate)**：Roflumilast、Alefacept、Alemtuzumab、Anakinra、Canakinumab，以及多種疫苗（破傷風類毒素、炭疽、腺病毒、霍亂活疫苗等）
  - **輕微 (Minor)**：各種鋅製劑
  - 整體而言，應避免與其他免疫抑制劑／生物製劑併用，並避免接種活疫苗。
- **潛在眼部發炎訊號**：文獻中出現貝賽特氏症病例及葡萄膜炎藥物警訊分析，使用於眼部疾病時需特別留意。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 類圓線蟲病為蠕蟲感染，與 IL-17RA 阻斷缺乏機轉連結，且免疫調節可能使寄生蟲控制惡化；預測僅來自模型，沒有試驗或文獻支持（L5）。
- 本次所有預測適應症（前 10 名）均維持 Hold，其中眼部發炎疾病雖有理論依據，但證據僅為前臨床與安全性訊號。

**若要推進需要：**
- 取得香港仿單的核准適應症、警語與禁忌症
- 補充藥物作用機轉資料（如 DrugBank）
- 若考慮眼部發炎疾病（如非感染性葡萄膜炎、視神經炎）：先界定明確的目標族群，並進行機轉與前臨床研究
- 評估眼部發炎相關安全性訊號，以及與克隆氏症／IBD 的禁忌風險
- 不建議針對類圓線蟲病投入進一步開發資源，除非有新的機轉證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

