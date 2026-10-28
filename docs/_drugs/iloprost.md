---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 458
evidence_level: L5
indication_count: 4
monitor_inn: "ILOPROST"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "pulmonary arteriovenous malformation (disease)", "diffuse alopecia areata"]
last_modified_at: 2026-10-28
description: "Iloprost：預測新適應症為單純性頭皮毛髮稀少症 (hypotrichosis simplex of the scalp)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Iloprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Iloprost: 單純性頭皮毛髮稀少症 (hypotrichosis simplex of the scalp)
{: .text-alpha }

## 一句話總結

Iloprost 是一種前列環素（prostacyclin）類似物，知識圖譜中記錄的原適應症為肺動脈高壓。
TxGNN 模型預測它可能對**單純性頭皮毛髮稀少症 (hypotrichosis simplex of the scalp)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 單純性頭皮毛髮稀少症 (hypotrichosis simplex of the scalp) |
| TxGNN 預測分數 | 0.9945 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Iloprost 是穩定的前列環素 (PGI2) 類似物，作用於 IP 受體，可使血管擴張並抑制血小板凝集。

理論上，血管擴張可能改善毛囊周圍微循環，而前列腺素訊號確實會影響毛髮週期（PGF2α、PGE2 類似物促進生長，PGD2 則抑制）。但 PGI2 對毛髮的作用尚未被證實。

此外，單純性毛髮稀少症是遺傳性疾病（如 CDSN、APCDD1、RPL21 等基因變異），血管擴張劑不太可能矯正根本缺陷。0.995 的高分只是模型預測，不等於有實際療效。

其他排名較前的預測同樣僅為模型輸出，且皆無試驗或文獻佐證：

| 排名 | 預測疾病 | TxGNN 分數 | 評語 |
|------|---------|-----------|------|
| 2 | 先天性毛髮稀少伴粟丘疹 (congenital hypotrichosis milia) | 0.9933 | 罕見遺傳性毛髮與皮膚疾病，無明確機轉依據 |
| 3 | 肺動靜脈畸形 (pulmonary arteriovenous malformation) | 0.9931 | 屬結構性血管分流，通常以栓塞治療；血管擴張甚至可能惡化分流或低血氧 |
| 4 | 瀰漫性圓禿 (diffuse alopecia areata) | 0.9910 | 屬自體免疫疾病，僅有鬆散的理論關聯，目前研發focus在 JAK 抑制劑 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50560 | ILOMEDIN 20 INJ 20MCG/ML | 注射劑 | 未載明 |

廠商為 BAYER HEALTHCARE LIMITED，屬單一成分製劑，狀態為有效。

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（非仿單內容）：肝衰竭、慢性阻塞性肺病（COPD）、低血壓、肺水腫、支氣管疾病。
- **藥物交互作用**：共查得 100 筆，以下為部分中度交互作用：
  - 擬交感神經類：Epinephrine、Ephedrine、Ephedrine（鼻用）、Fenfluramine、Dexfenfluramine、Sibutramine
  - SGLT2 抑制劑：Canagliflozin、Dapagliflozin、Empagliflozin、Ertugliflozin
  - 其他：Acetylsalicylic acid（阿斯匹靈）、吸入型速效胰島素、Mannitol、Glycerin、Papaverine

完整警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 四個預測適應症皆無臨床試驗或文獻支持，證據等級為 L5，且遺傳性毛髮稀少症的病因與血管擴張機轉缺乏明確關聯。
- 此藥在知識圖譜中被記錄有低血壓等禁忌關聯，若無明確效益依據，不宜推進。

**若要推進需要：**
- 取得 DrugBank 的作用機轉資料，並評估 PGI2 訊號與毛囊的機轉關聯
- 取得香港衛生署仿單，釐清警語與禁忌
- 進行前臨床研究（如毛囊培養或動物模型），確認對毛髮生長是否有作用
- 釐清給藥途徑：目前香港僅有注射劑型，用於頭皮疾病的可行性（如局部給藥）尚待評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

