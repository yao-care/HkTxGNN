---
layout: default
title: Isoniazid
parent: 中證據等級 (L3-L4)
nav_order: 416
evidence_level: L4
indication_count: 1
---

# Isoniazid
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Isoniazid：從結核病（含潛伏結核感染）到結膜炎

## 一句話總結

Isoniazid 是經典抗結核病藥物，原用於治療結核病與潛伏結核感染（LTBI）。
TxGNN 模型預測它可能對**結膜炎 (Conjunctivitis)** 有效，預測分數高達 **99.36%**，
但目前僅有 **1 個臨床試驗**（與結膜炎主題無關）和 **20 篇文獻**（多為結核性眼部感染個案或藥物不良反應報告）支持，機轉分析顯示此預測可能是知識圖譜的混淆信號。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 結核病／潛伏結核感染（LTBI）（依文獻與試驗背景推斷，無正式核准適應症紀錄） |
| 預測新適應症 | 結膜炎 (Conjunctivitis) |
| TxGNN 預測分數 | 99.36% |
| 證據等級 | L4 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 isoniazid 的詳細作用機轉（MOA）資料。根據現有文獻脈絡，isoniazid 是抑制結核桿菌細胞壁合成的抗結核藥物，其「與結膜炎相關」的文獻案例實際上分屬三種情況：(1) 結膜結核感染——isoniazid 作為抗結核治療延伸至眼部病灶，屬原適應症範圍而非新用途；(2) isoniazid 本身引發的眼部藥物不良反應個案；(3) BCG 膀胱灌注免疫治療後併發的反應性關節炎/多關節炎，與結膜炎僅間接相關（Reiter 症候群樣反應）。

換言之，**目前沒有證據支持 isoniazid 對一般性（病毒性/過敏性/細菌性）結膜炎具有治療效果**。TxGNN 給出的高分很可能是知識圖譜中「isoniazid－結核－結膜」共現路徑造成的混淆信號，而非真實的藥理適應性。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | 完成 | 490 | 比較 3HP（rifapentine+isoniazid）與 1HP 方案用於潛伏結核感染（LTBI）預防性治療的全身性藥物不良反應發生率；**與結膜炎治療無關**（相關性評級 C，僅因使用 isoniazid 而被收錄） |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optometry Clinics | 系統性回顧藥物引起的眼部副作用，提及 isoniazid 相關藥物可能與結膜炎/瞼結膜炎有關（非治療效果） |
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Case Report | Am Rev Respir Dis | 阿拉斯加愛斯基摩人瞼結膜炎（phlyctenular keratoconjunctivitis）流行病學與 isoniazid 預防性投藥觀察 |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Case Report | Annales d'oculistique | Isoniazid 局部治療眼部結核病之應用 |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Case Report | Cornea | 結核分枝桿菌感染表現為慢性紅眼（結膜結核） |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case Report | Middle East Afr J Ophthalmol | 義眼窩結核性結膜炎個案 |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case Report | Medicine | 兒童鼻竇原發性結核合併瞼結膜炎個案 |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Case Report | Can J Ophthalmol | 結膜瞼裂腫為潛在臨床結核病之前驅表徵 |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case Report | Arch Ophthalmol | 原發性結膜結核病個案 |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Case Report | Oftalmologia | 瞼裂性角結膜炎與淋巴結結核病關聯之 28 例回顧 |
| [32674602](https://pubmed.ncbi.nlm.nih.gov/32674602/) | 2020 | Case Report | Clinical Pediatrics | 青少年結膜炎之非典型病因個案報告 |

> 上述文獻多為結核性眼部感染或藥物副作用個案報告，**無任何研究直接顯示 isoniazid 對一般結膜炎具治療效果**。

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：TFDA/香港仿單警語與禁忌資料目前缺失（屬 Blocking 等級資料缺口），此為進入 S1 安全性初評的必要前提。

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉分析顯示此預測很可能是知識圖譜中「isoniazid－結核－結膜」共現路徑造成的混淆信號，而非真實藥理效果。
- 現有臨床試驗與結膜炎治療目的無關，文獻證據以結核性眼部感染個案與藥物不良反應報告為主，未達到支持適應症擴展的證據強度（決策階段仍為 S0）。

**若要推進需要：**
- 補齊 isoniazid 的作用機轉（MOA）資料
- 取得 TFDA/香港仿單完整警語與禁忌症資料（目前為 Blocking 缺口）
- 針對「結膜炎」（而非結核性眼部感染）設計專屬的前臨床或機轉研究，以排除知識圖譜混淆信號的可能性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

