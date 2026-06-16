---
layout: default
title: Hesperidin
parent: 中證據等級 (L3-L4)
nav_order: 369
evidence_level: L4
indication_count: 10
---

# Hesperidin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Hesperidin：從天然柑橘黃酮到骨髓增生性腫瘤

## 一句話總結

Hesperidin（橙皮苷）是廣泛存在於柑橘類水果中的天然黃酮醇苷，目前無任何已核准適應症。
TxGNN 模型預測它可能對**骨髓增生性腫瘤 (Myeloproliferative Neoplasm)** 有效，
目前有 **0 個臨床試驗**和 **2 篇文獻**支持此方向，且兩篇均屬間接或代謝物研究，不足以進入安全性評估階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無核准適應症（天然食品來源化合物） |
| 預測新適應症 | 骨髓增生性腫瘤 (Myeloproliferative Neoplasm) |
| TxGNN 預測分數 | 99.47% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Hesperidin 是柑橘類水果（橙子、柚子、檸檬）果皮中含量最豐的多酚黃酮苷，在體內被腸道菌群水解後代謝為活性更高的苷元 Hesperetin（橙皮素）。由於缺乏已核准適應症，其官方作用機轉資料（MOA）尚為資料缺口；廣泛文獻顯示其具有抗氧化、抗炎、抗增殖等多效特性。

骨髓增生性腫瘤（MPN）是一類造血幹細胞的克隆性疾病，涵蓋慢性骨髓性白血病（CML）、真性紅血球增多症（PV）、原發性血小板增多症（ET）及原發性骨髓纖維化（PMF）。TxGNN 的高預測分數（0.9947）主要反映知識圖譜中骨髓惡性腫瘤節點的網路拓樸推算——計算研究（in silico）預測 Hesperidin 可結合 BCR 激酶結構域（BCR-ABL 融合蛋白是 CML 驅動突變），但廣義 MPN 亞型的直接體外或體內實驗數據幾乎完全缺失。

值得注意的是，在更廣泛的骨髓性白血病（本報告 Rank 8）範疇，現有體外研究已在 K562（CML）、HL-60（AML）、KG-1（AML）及 NB4（APL）細胞株中記錄到 Hesperidin 及 Hesperetin 的抗腫瘤活性，顯示黃酮類成分針對骨髓性惡性腫瘤具有一定生物學合理性。然而多數研究主角為代謝物 Hesperetin 而非 Hesperidin 本身，Hesperidin 的口服生物可用率（oral bioavailability）偏低是未來臨床轉化的關鍵障礙。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31759365](https://pubmed.ncbi.nlm.nih.gov/31759365/) | 2019 | In silico（分子對接） | Asian Pacific Journal of Cancer Prevention | 計算方法預測 Hesperidin 可結合 BCR 激酶結構域，具抑制 CML 中 Grb-2/BCR-ABL 交互作用、對抗 TKI 藥物抗性的潛力 |
| [40751800](https://pubmed.ncbi.nlm.nih.gov/40751800/) | 2025 | In vitro（細胞株） | Medical Oncology | Hesperetin（代謝物）可上調人類骨髓白血病細胞膜黃體素受體（mPR）表達並顯著降低 ROS，具抗氧化與潛在抗腫瘤活性 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
針對 MPN 的直接臨床試驗完全缺失，現有 2 篇文獻均屬間接研究（一篇為純計算方法，一篇以代謝物 Hesperetin 為研究主角），不符合進入 S1 安全性初評的最低門檻。此外，Hesperidin 的 MOA 及安全性資料均存在明確資料缺口（Blocking/High severity），無法進行完整的安全性評估。

**若要推進需要：**
- 補充 Hesperidin 的作用機轉資料（DrugBank MOA 查詢）
- 取得 Hesperidin（而非代謝物 Hesperetin）特異性的 MPN 或廣義骨髓性腫瘤體外實驗數據
- 評估 Hesperidin 口服生物可用率與體內有效血漿濃度（PK/PD 資料）
- 完成安全性資料收集（TFDA 仿單警語與禁忌症）
- 優先考慮以**骨髓性白血病（Rank 8，L4，Research Question）**為研究切入點，該適應症擁有 16 篇體外研究文獻，生物學機轉較完整，具備開展正式研究問題的初步依據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

