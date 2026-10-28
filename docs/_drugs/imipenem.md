---
layout: default
title: Imipenem
parent: 僅模型預測 (L5)
nav_order: 463
evidence_level: L5
indication_count: 10
monitor_inn: "IMIPENEM"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "sinusitis", "chronic rhinosinusitis", "typhoid fever", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "staphylococcus aureus infection", "eosinophilia-myalgia syndrome"]
last_modified_at: 2026-10-28
description: "Imipenem：預測新適應症為瀰漫性硬皮症 (Diffuse Scleroderma)（證據等級 L5）。原適應症：香港許可證資料未載明適應症文字"
---

# Imipenem
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

## Imipenem：從細菌感染到瀰漫性硬皮症
{: .text-alpha }

## 一句話總結

Imipenem 是碳青黴烯類（carbapenem）抗生素，知識圖譜記錄的原用途為細菌性肺炎、腹膜炎、心內膜炎等細菌感染。
TxGNN 模型預測它可能對**瀰漫性硬皮症 (Diffuse Scleroderma)** 有效，但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測，機轉上也缺乏合理連結。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明適應症文字；知識圖譜記錄的關聯為細菌性肺炎、腹膜炎、鏈球菌性肺炎、心內膜炎、細菌性關節炎、子宮內膜炎等（僅為知識圖譜關聯，非許可證核准內容） |
| 預測新適應症 | 瀰漫性硬皮症 (Diffuse Scleroderma) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Imipenem 屬於碳青黴烯類 β-內醯胺抗生素，一般認為是透過抑制細菌細胞壁合成而殺菌。

瀰漫性硬皮症是一種自體免疫性、纖維化疾病，沒有已知的細菌性驅動因素。因此，抗菌機轉與此疾病之間**看不出合理的機轉連結**。極高的分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而不是生物學證據。

這項預測只能視為模型輸出，不應視為有實質支持的再利用假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53560 | PREPENEM FOR INJ 500MG | 未載明 | 未載明 |
| HK-61317 | PRIMAGAL POWDER FOR SOLUTION FOR INFUSION 500/500MG | 未載明 | 未載明 |
| HK-66808 | IMCIMILL POWDER FOR SOLUTION FOR INFUSION 500MG/500MG | 未載明 | 未載明 |
| HK-64660 | IMIPENEM/CILASTATIN KABI POWDER FOR SOLUTION FOR INFUSION 500MG/500MG | 未載明 | 未載明 |

以上 4 張許可證目前均為有效狀態，許可證資料中沒有適應症文字。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（來自知識圖譜的藥物－疾病關聯，非仿單文字）：癲癇、腎臟疾病、輸尿管積膿、困難梭狀芽孢桿菌結腸炎、新生兒壞死性腸炎。
- **藥物交互作用**：共查得 15 項。
  - 嚴重（Major）：Bupropion、Iohexol、Iopamidol。
  - 中度（Moderate）：Warfarin、Dicoumarol、Theophylline、Aminophylline、Dyphylline、Oxtriphylline、Cyclosporine、Mycophenolic acid、Pemetrexed、Ethinylestradiol、Lindane、含電解質之聚乙二醇 3350。

完整警語與禁忌請參考原廠仿單。

## 其他預測方向的補充觀察

本報告以排名第一的預測（瀰漫性硬皮症）為主。其他預測適應症中，以下兩項值得留意：

| 預測適應症 | 證據概況 | 備註 |
|-----------|---------|------|
| 金黃色葡萄球菌感染 | 2 項 Phase 4 試驗（含 NCT00871104：fosfomycin + imipenem 用於 MRSA 心內膜炎，已完成，n=50），另有小型病例研究與案例評論 | 皆為合併療法且樣本小，無法證明 imipenem 單獨有效；若推進須限於難治性 MRSA 的合併治療並受抗生素管理監督 |
| 傷寒／副傷寒／沙門氏菌病 | 僅有體外感受性調查與病例報告，無臨床試驗 | 碳青黴烯類可作為廣泛抗藥傷寒的後備選項，屬待研究問題 |

其餘預測（鼻竇炎類、鼻竇腫瘤、嗜酸性球增多肌痛症候群）證據薄弱或缺乏合理機轉。

## 結論與下一步

**決策：Hold**

**理由：**
- 瀰漫性硬皮症沒有任何臨床試驗或文獻支持，抗菌機轉與自體免疫纖維化疾病也無合理連結，僅有模型預測分數，屬 L5。

**若要推進需要：**
- 提出可驗證的機轉假說，例如抗菌以外的免疫調節作用，並以前臨床研究驗證
- 取得完整的作用機轉資料
- 取得香港仿單的警語與禁忌資料
- 若要優先投入資源，建議改評估證據較充分的細菌感染方向（如難治性 MRSA 合併療法）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

