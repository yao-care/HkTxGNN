---
layout: default
title: Quetiapine
parent: 僅模型預測 (L5)
nav_order: 627
evidence_level: L5
indication_count: 5
---

# Quetiapine
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

# QUETIAPINE：從精神疾病用藥到視網膜萎縮症合併眼外異常

## 一句話總結

Quetiapine（喹硫平）是一種非典型抗精神病藥，目前尚未在香港取得藥品許可證。
TxGNN 模型預測它可能對**視網膜色素失養症合併/不合併眼外異常 (Retinal Dystrophy with or without Extraocular Anomalies)** 有效，
但目前**無臨床試驗**、**15 篇文獻中無一篇實際提及 quetiapine**，機轉合理性亦被判定為低。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未提供（香港未上市；已知為非典型抗精神病藥） |
| 預測新適應症 | 視網膜色素失養症合併/不合併眼外異常 (Retinal Dystrophy with or without Extraocular Anomalies) |
| TxGNN 預測分數 | 99.57%（排名第 8077） |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Quetiapine 的主要藥理機轉為 D2 及 5-HT2A 受體拮抗，作用於中樞神經傳導路徑，臨床上用於精神分裂症、雙相情感障礙等精神疾病。目前缺乏更詳細的作用機轉資料（DrugBank MOA 欄位未提供）。

視網膜色素失養症合併眼外異常屬於**先天性、結構性/遺傳性疾病**，病因多為基因突變導致眼球發育缺陷，與神經傳導物質受體調節在生物學上沒有已知關聯。

進一步檢視支持文獻後發現，15 篇被 PubMed 檢索到的文獻雖與「視網膜/眼外異常」主題相關（眼眶感染、複視、先天性眼瞼下垂、水晶體異常等眼科案例報告與回顧），但**沒有一篇摘要實際提及 quetiapine**。這顯示 TxGNN 給出的高分（0.9957）很可能是知識圖譜中 quetiapine 與其他精神/神經節點連結所產生的雜訊擴散，而非真正的藥理學關聯，證據包本身的機轉分析也持相同結論。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

⚠️ 以下文獻經 TxGNN 疾病關鍵字檢索匹配，但**摘要中均未提及 quetiapine**，僅供背景參考，不構成機轉支持證據。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | 眼眶感染之病因與分期回顧，未涉及藥物治療 |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | 複視之臨床評估方法，非藥物介入相關 |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | 先天性水晶體形狀異常之回顧 |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler 症候群複合體之眼科表現 |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Archives of Ophthalmology | 眼眶動靜脈畸形之臨床特徵與處置 |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | 小兒眼眶病灶之影像學鑑別診斷 |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Case Report | Klinische Monatsblätter für Augenheilkunde | 先天性眼瞼下垂之分型與治療考量 |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | American Journal of Ophthalmology | 單側隱眼畸形（cryptophthalmia）病例報告 |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | Journal of Neuro-Ophthalmology | 先天性滑車—動眼神經聯帶運動病例 |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case Report | Optometry and Vision Science | 先天性眼外肌纖維化合併變異性協同性外展 |

## 香港上市資訊

Quetiapine 目前**未在香港取得藥品許可證**，無上市資料可供列出。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅 L5（純模型預測），無任何臨床試驗支持，15 篇文獻檢索結果均與 quetiapine 無直接關聯。
- 預測適應症為先天性結構性疾病，與 quetiapine 已知的受體拮抗機轉缺乏生物學合理性，證據包內部分析亦判定為知識圖譜雜訊可能性高。
- 藥物在香港尚未上市，缺乏本地安全性與法規資料。
- 同一評估批次中其餘 4 個候選適應症（醣基化缺陷症、水腦畸形、17p13.3 微缺失症候群、多小腦回症候群）亦均為 L5、無實證支持，建議一併保留（Hold）。

**若要推進需要：**
- 補齊 Quetiapine 完整作用機轉（MOA）與 DrugBank 分類資料
- 取得原廠仿單警語、禁忌症及 DDI 資料
- 尋找是否有實際將 quetiapine 用於眼科/視網膜疾病的機轉研究或病例報告，以驗證 TxGNN 分數是否具生物學意義
- 若無法找到機轉層級支持，建議將此預測標記為低優先級雜訊候選
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

