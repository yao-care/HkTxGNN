---
layout: default
title: Prochlorperazine
parent: 僅模型預測 (L5)
nav_order: 721
evidence_level: L5
indication_count: 10
---

# Prochlorperazine
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

# Prochlorperazine：從（原適應症資料未載明）到視網膜營養不良

## 一句話總結

Prochlorperazine 是一種吩噻嗪（phenothiazine）類藥物，在香港已有 12 張許可證，但所取得的資料中沒有記載原核准適應症。
TxGNN 模型預測它可能對**視網膜營養不良（伴或不伴眼外異常）**有效，預測分數很高（99.998%）。
不過目前**沒有任何臨床試驗**，檢索到的 15 篇文獻也都沒有提到本藥，證據僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 視網膜營養不良，伴或不伴眼外異常 (Retinal dystrophy with or without extraocular anomalies) |
| TxGNN 預測分數 | 99.998% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 12 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Prochlorperazine 屬於吩噻嗪類藥物，依藥物類別推測，其作用與多巴胺 D2 受體拮抗有關。這是依類別推論，並非取自本次資料。

視網膜營養不良是遺傳性視網膜退化疾病，屬於基因與結構層面的病變。目前沒有任何證據顯示 D2 拮抗作用能改變這類疾病的病程，因此機轉上並無已知的連結。

TxGNN 分數很高，但它只代表知識圖譜上的關聯，不代表藥效。檢索到的文獻主要談眼外肌與眼眶疾病，看起來是疾病關鍵字的比對結果，不是藥物與疾病之間的證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下 10 篇為檢索結果中的代表性文獻，皆為疾病背景類文獻，**沒有一篇提到 prochlorperazine 或其治療效果**。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | 複視的系統性問診與檢查方法 |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | 眼眶感染多由鼻竇炎引起，臨床表現包括眼球突出、眼球運動受限 |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblatter fur Augenheilkunde | 先天性眼瞼下垂的型態、合併症與檢查原則 |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | 先天性水晶體形狀異常的分類與表現 |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | 小兒眼部病變的鑑別診斷與影像特徵 |
| [10192514](https://pubmed.ncbi.nlm.nih.gov/10192514/) | 1999 | Review | Progress in Retinal and Eye Research | 眼外肌本體感受器及其在視覺空間感知中的角色 |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | Journal of Binocular Vision and Ocular Motility | 先天性顱神經失神經支配疾病與眼肌麻痺 |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | American Journal of Ophthalmology | 兩例單側隱眼畸形的臨床特徵 |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | 未分類 | International Journal of Molecular Sciences | 先天性眼外肌纖維化合併視神經乳頭與視網膜異常 |
| [31359131](https://pubmed.ncbi.nlm.nih.gov/31359131/) | 2019 | 未分類 | Human Genetics | 視黃酸訊息路徑相關的眼部發育缺陷之遺傳架構 |

---

## 香港上市資訊

本藥在香港共有 12 張許可證，以下列出 5 張主要許可證。取得的資料中未載明劑型與核准適應症。

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-46144 | SERATIL TAB 5MG (WHITE) | CHRISTO PHARM LTD |
| HK-06335 | METIL TAB 5MG | VICKMANS LABORATORIES LTD |
| HK-61940 | PROCHLOR TABLETS 5MG | WAI LUN TRADING CO |
| HK-11609 | PERATIL TAB 5MG (BLUE) | SYNCO (H.K.) LIMITED |
| HK-50611 | METIL-B TAB 5MG | VICKMANS LABORATORIES LTD |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測只來自模型分數，沒有臨床試驗，檢索到的文獻也與本藥無關，證據等級為 L5。
- 此疾病為遺傳性視網膜退化，沒有合理的藥理機轉支持，且安全性資料尚未取得。

**若要推進需要：**
- 取得香港衞生署的仿單，確認核准適應症、警語與禁忌。
- 補齊 DrugBank 的作用機轉資料，再評估與視網膜營養不良之間有無機轉連結。
- 針對本藥與視網膜疾病重新做精準文獻檢索，並確認有無前臨床研究。
- 其他預測中，**躁期雙相情緒障礙**（排名 10，L4）可作為較值得研究的方向，因為多巴胺 D2 拮抗劑與抗精神病藥物有類別上的關聯。目前只有類別層級與歷史安全性報告，缺乏療效證據，需先評估是否優於現有核准藥物，並留意癲癇閾值、錐體外症狀與遲發性運動障礙等風險。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

