---
layout: default
title: Ripretinib
parent: 僅模型預測 (L5)
nav_order: 652
evidence_level: L5
indication_count: 10
---

# Ripretinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Ripretinib：從腸胃道基質瘤（GIST）到多發性內分泌腫瘤

## 一句話總結

Ripretinib 是一種 switch-control 別構抑制劑，鎖定 KIT 與 PDGFRA 酪胺酸激酶，已知用於晚期腸胃道基質瘤（GIST）的四線治療（香港尚未上市）。TxGNN 模型將「多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)」列為分數最高的預測適應症（**98.84%**），但目前**無任何臨床試驗或文獻**支持，機轉分析判斷此為知識圖譜的偽陽性預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腸胃道基質瘤 (GIST)，晚期四線治療（此為已知用藥情境，未列於本次結構化資料中） |
| 預測新適應症 | 多發性內分泌腫瘤 (Multiple Endocrine Neoplasia) |
| TxGNN 預測分數 | 98.84% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為資料缺口）。根據既有文獻與已知藥理分類，Ripretinib 是一種 switch-control 別構抑制劑，鎖定 KIT/PDGFRA 酪胺酸激酶，其在腸胃道基質瘤 (GIST) 的療效已獲證實。

多發性內分泌腫瘤 (MEN) 症候群主要致病基因為 RET（MEN2A/2B）與 MEN1，其訊息傳導路徑與 KIT/PDGFRA 並無已知交集。TxGNN 給出的高分（98.84%）在知識圖譜方法中，較可能反映拓樸結構相似性，而非真實生物學關聯。

本評估的機轉分析結論明確指出：此預測**缺乏機轉基礎**，且無任何支持性臨床試驗或文獻，判斷為模型高分但無機轉基礎的偽陽性預測，不建議以此適應症作為後續開發方向。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 其他預測適應症（Rank 2–10）總覽

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策 | 備註 |
|------|-----------|-----------|---------|------|------|
| 2 | HER2 positive breast carcinoma | 98.32% | L5 | Hold | 機轉無重疊，唯一文獻為不相關之激酶抑制劑總覽 |
| 3 | malignant catarrh | 98.32% | L5 | Hold | 牛隻疱疹病毒疾病，判斷為圖譜實體誤配 |
| 4 | infectious bovine rhinotracheitis | 98.32% | L5 | Hold | 牛傳染性鼻氣管炎，非人類疾病，圖譜實體誤配 |
| 5 | cytomegalovirus infection | 98.23% | L5 | Hold | 無機轉關聯，無支持性證據 |
| 6 | amenorrhea (disease) | 97.79% | L5 | Hold | 僅為推測性副作用機轉，非治療性適應症 |
| 7 | progesterone-receptor negative breast cancer | 97.63% | L5 | Hold | 機轉無交集，無證據 |
| 8 | normal breast-like subtype of breast carcinoma | 97.59% | L5 | Hold | 機轉無交集，無證據 |
| 9 | progesterone-receptor positive breast cancer | 97.59% | L5 | Hold | 機轉無交集，無證據 |
| 10 | breast tumor luminal A or B | 97.55% | L5 | Hold | 附帶 19 篇文獻經查證均為 B 細胞發育、B 肝疫苗、HLA-B 等主題，屬關鍵字（字母 "B"）誤配噪音，不具證據價值 |

**結論：全部 10 個候選適應症均為 Hold，無一具備機轉基礎或支持性證據。**

## 香港上市資訊

目前無許可證登記（香港未上市）

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（KIT/PDGFRA 激酶抑制劑，switch-control 別構抑制劑；非傳統細胞毒性化療藥物） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 雖給出高分（98.84%），但機轉分析、臨床試驗及文獻檢索均未發現支持性證據，判斷為知識圖譜偽陽性預測；其餘 9 個候選適應症同樣缺乏機轉基礎與證據。
- 原廠仿單警語、禁忌症（Blocking 級別缺口）與 MOA 詳細資料（High 級別缺口）均缺失，無法進入 S1 安全性初評階段。

**若要推進需要：**
- 向 TFDA/原廠取得完整仿單警語與禁忌症資料（解除 DG001）
- 透過 DrugBank API 補齊詳細作用機轉資料（解除 DG002）
- 若未來出現支持性文獻或試驗，針對該適應症重新進行機轉關聯性評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

