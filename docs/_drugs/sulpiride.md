---
layout: default
title: Sulpiride
parent: 僅模型預測 (L5)
nav_order: 826
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

# Sulpiride：從（原適應症未載明）到視網膜失養症

## 一句話總結

Sulpiride 是選擇性 D2/D3 多巴胺受體拮抗劑，在香港已有 6 張許可證上市。
TxGNN 模型預測它可能對**視網膜失養症（retinal dystrophy with or without extraocular anomalies）**有效，
但目前**沒有臨床試驗**，文獻也未直接涉及 sulpiride，僅為模型預測，證據等級 L5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供 |
| 預測新適應症 | 視網膜失養症 (retinal dystrophy with or without extraocular anomalies) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位未提供）。依分析資料，sulpiride 是選擇性 D2/D3 多巴胺受體拮抗劑。視網膜中的多巴胺訊號會調節光受器耦合與晝夜節律功能，這是兩者之間唯一可想像的關聯。

不過，目前沒有任何證據顯示阻斷 D2/D3 能減緩或治療遺傳性視網膜病變。99.95% 的高分只是知識圖譜的推論，缺乏臨床或前臨床資料支持，應視為待驗證的假說，而非有根據的新用途。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下列文獻是以預測疾病相關詞彙檢索而得，內容談的是眼眶、眼外肌及先天性眼部異常，並未討論 sulpiride，也未提供任何療效證據。以下僅列出 10 篇（依 Review 優先、再列 Case report 排序）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | 眼眶感染的病因（以鼻竇炎最常見）與臨床表現 |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | 複視的系統性問診與檢查方法 |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | 先天性眼瞼下垂的型態與檢查 |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | 先天性水晶體形狀異常 |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler 症候群的玻璃體視網膜病變 |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | 小兒眼部病變的鑑別診斷與影像特徵 |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Arch Ophthalmol | 眼眶動靜脈畸形的臨床特徵與處置 |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | Am J Ophthalmol | 單側隱眼畸形兩例 |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | J Neuroophthalmol | 先天性滑車神經—動眼神經聯合運動一例 |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case report | Optom Vis Sci | 先天性眼外肌纖維化病人的協同性外散一例 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65024 | GAMOTIL CAPSULES 50MG | 未提供 | 未提供 |
| HK-53702 | VICK-SULPIRIDE CAP 50MG | 未提供 | 未提供 |
| HK-40717 | SULPIREN TAB 50MG | 未提供 | 未提供 |
| HK-52650 | SUPIDE CAP 50MG | 未提供 | 未提供 |
| HK-44716 | SULIDE CAP 50MG | 未提供 | 未提供 |

## 安全性考量

- **藥物交互作用**：查詢無結果。
- **其他風險（模型推論，非仿單資料）**：Sulpiride 可能造成高泌乳素血症與錐體外症狀，對神經病變族群需特別留意。

主要警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
只有模型預測，沒有臨床試驗，所附文獻也未涉及 sulpiride。機轉上也無支持 D2/D3 阻斷可治療遺傳性視網膜病變的依據。

**若要推進需要：**
- 補齊 sulpiride 的作用機轉資料（DrugBank）
- 取得香港衞生署仿單，確認警語與禁忌症
- 進行視網膜多巴胺—D2/D3 拮抗與視網膜退化的前臨床文獻回顧
- 在動物或細胞模型中取得初步證據，再考慮臨床試驗

另外，其他預測適應症（水腦無腦症、多小腦回畸形合併小腦發育不全與關節攣縮、Charcot-Marie-Tooth 1G 型、X 連鎖近視）同樣只有模型分數、無任何證據，建議同為 Hold。其中 X 連鎖近視在機轉上可能反向（D2 拮抗劑預期不利於控制近視）。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

