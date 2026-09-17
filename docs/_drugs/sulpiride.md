---
layout: default
title: Sulpiride
parent: 僅模型預測 (L5)
nav_order: 713
evidence_level: L5
indication_count: 5
---

# Sulpiride
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

# Sulpiride：原適應症資料缺失 → 視網膜失養症（伴或不伴眼外異常）

## 一句話總結

> Evidence Pack 中未提供 Sulpiride 的原適應症與香港上市許可證紀錄。
> TxGNN 模型預測它可能對**視網膜失養症，伴或不伴眼外異常 (Retinal Dystrophy with or without Extraocular Anomalies)** 有效，
> 目前**無臨床試驗**登記，僅有 **15 篇文獻**與疾病主題相關，但皆未實際研究 Sulpiride 本身。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（未提供許可證或核准適應症紀錄） |
| 預測新適應症 | 視網膜失養症，伴或不伴眼外異常 |
| TxGNN 預測分數 | 99.95%（排名 1442） |
| 證據等級 | L5（僅模型預測，文獻未直接佐證藥物－疾病關聯） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Sulpiride 的詳細作用機轉（MOA）資料（DG002），且無原適應症或香港上市登記紀錄可供對照，因此無法建立機轉層面的關聯性分析。

TxGNN 分數雖高（99.95%），但此分數僅反映知識圖譜中藥物與疾病節點間的拓樸關聯性，不代表已有生物學或臨床證據支持。此點在同一份 Evidence Pack 中的其他候選適應症也得到印證——例如排名第 4 的 Charcot-Marie-Tooth disease type 1G，其評分結果已明確標註「無臨床試驗、無文獻佐證，機轉上與藥物已知作用無明確重疊」，建議為 Hold。整體而言，本批預測目前僅停留在模型層級，尚無實質證據支撐。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | 未分類 | Semin Ultrasound CT MR | 眼眶感染分期與臨床表現綜述 |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | 未分類 | Semin Neurol | 複視之鑑別診斷方法 |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | 未分類 | Klin Monbl Augenheilkd | 先天性上瞼下垂之分類與治療 |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | 未分類 | Taiwan J Ophthalmol | 先天性水晶體形狀異常綜述 |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | 未分類 | Am J Ophthalmol | 單側隱眼畸形病例報告 |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | 未分類 | J Neuroophthalmol | 先天性滑車－動眼神經共動症病例 |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | 未分類 | Doc Ophthalmol | Wagner-Stickler 症候群綜合描述 |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | 未分類 | Pediatr Radiol | 兒童眼眶病灶之影像鑑別 |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | 未分類 | Optom Vis Sci | 先天性眼外肌纖維化病例報告 |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | 未分類 | Arch Ophthalmol | 眼眶動靜脈畸形之臨床特徵 |

**重要提醒**：以上文獻皆標註為 `pending`（未分類、相關性未判定），且經摘要檢視，內容均為一般眼科／先天性眼部異常之臨床描述，**未見任何一篇實際研究 Sulpiride**。這批文獻疑似僅透過疾病關鍵詞比對產生，尚不足以構成藥物－疾病關聯的實質證據。

## 香港上市資訊

目前無香港上市許可證資料（市場狀態：未上市）。

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：TFDA/香港仿單警語與禁忌症資料為 Blocking 等級缺口（DG001），在此資料補齊前無法進入 S1 安全性初評階段。

## 結論與下一步

**決策：Hold**

**理由：**
- 無任何臨床試驗支持；15 篇相關文獻經檢視後均未實際研究 Sulpiride，僅為疾病背景資料。
- 缺乏作用機轉（MOA）資料與原適應症/上市紀錄，無法建立機轉關聯性假說。
- 安全性資料存在 Blocking 缺口，無法進行初步安全性評估。

**若要推進需要：**
- 補齊 TFDA／香港藥監局仿單安全性資料（DG001，Blocking，來源：官方仿單 PDF）
- 取得 Sulpiride 作用機轉資料（DG002，High，來源：DrugBank API）
- 對現有 15 篇文獻重新篩選，確認是否存在真正探討 Sulpiride 與視網膜/眼科疾病關聯的研究
- 若上述資料補齊後仍無直接證據，建議暫緩此候選適應症的後續評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

