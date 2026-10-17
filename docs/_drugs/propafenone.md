---
layout: default
title: Propafenone
parent: 僅模型預測 (L5)
nav_order: 738
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Propafenone：預測新適應症為躁症（Manic bipolar affective disorder）（證據等級 L5）。原適應症：心房顫動、心室心搏過速"
monitor_inn: "Propafenone"
predicted_indications: ["manic bipolar affective disorder", "periodic paralysis with transient compartment-like syndrome", "Prinzmetal angina", "arrhythmogenic right ventricular cardiomyopathy", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania"]
---

# Propafenone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Propafenone：從心房顫動與心室心搏過速到兒茶酚胺敏感性多形性心室心搏過速

## 一句話總結

Propafenone 是 IC 類抗心律不整藥物，原本用於心房顫動與心室心搏過速。
TxGNN 模型預測分數最高的是躁症（manic bipolar affective disorder），但文獻只顯示它可能誘發躁症，並不支持療效。
證據最完整的方向是**兒茶酚胺敏感性多形性心室心搏過速 (CPVT)**：目前無臨床試驗登記，有 **10 篇文獻**（含前臨床機轉研究、世代研究與個案報告）。

> 說明：預測清單共 8 項。本報告的快速總覽與證據表以排名第 1 的躁症為準，因為這是模型分數最高者，但證據不支持。後面另列證據最強的 CPVT 供評估參考。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心房顫動、心室心搏過速（取自知識圖譜，香港許可證未載明適應症文字） |
| 預測新適應症 | 躁症（Manic bipolar affective disorder） |
| TxGNN 預測分數 | 99.80% |
| 證據等級 | L5（僅模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

**其他預測適應症一覽**

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 1 | 躁症 | 99.80% | L5 | Hold |
| 2 | 兒茶酚胺敏感性多形性心室心搏過速 (CPVT) | 99.79% | L3 | 列為研究問題（Research Question） |
| 3 | 週期性麻痺合併暫時性腔室樣症候群 | 99.67% | L5 | Hold |
| 4 | 變異型心絞痛 (Prinzmetal angina) | 99.45% | L5 | Hold |
| 5 | 嬰兒持續性心室心搏過速 | 99.44% | L3 | 列為研究問題（Research Question） |
| 6 | 致心律不整性右心室心肌病變 (ARVC) | 99.42% | L4 | Hold |
| 7 | 腎因性抗利尿不適當症候群 | 99.23% | L5 | Hold |
| 8 | 拔毛症 | 99.17% | L5 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Propafenone 屬於 IC 類（鈉離子通道阻斷）抗心律不整藥物，其在心房顫動與心室心搏過速的療效已被證實。

**躁症（排名 1）：** 機轉上沒有合理的治療連結。1985 年個案報告指出 Propafenone 可能引發躁症，作者推測它與抗憂鬱藥 bupropion 化學結構相關。2001 年另有 Propafenone 與 venlafaxine 交互作用導致器質性精神病的報告。這些都是不良反應訊號，不支持再利用。高分數缺乏臨床證據支持。

**CPVT（排名 2）：** 機轉上相當合理。CPVT 與 RyR2 鈣離子釋放通道異常有關。前臨床研究（PMID 21270101、26121139、21798265）顯示 flecainide 與 Propafenone（含 R-propafenone）等 I 類藥物可抑制 RyR2 通道、抑制鈣波。Flecainide 已作為 CPVT 的附加療法，Propafenone 有類似機轉。另有一份長達 35 年有效治療的個案報告（PMID 30820400）。

**其他方向：** 嬰兒持續性心室心搏過速與原適應症高度重疊，較像適應症延伸而非真正再利用。ARVC 則有 Propafenone 誘發 QRS 增寬與持續性心室心搏過速的安全疑慮。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

**躁症（排名 1）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Review | Pharmacological Reports | 評估抗精神病藥與心血管藥物之間的有害交互作用 |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Case report | Int J Psychiatry Med | 雙相情感障礙患者因 venlafaxine 與 Propafenone 交互作用出現器質性精神病 |
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Case report | J Clin Psychiatry | Propafenone 引發躁症，屬不良反應 |

**CPVT（證據最強的預測方向，供參考）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21270101](https://pubmed.ncbi.nlm.nih.gov/21270101/) | 2011 | 前臨床/機轉 | Circ Arrhythm Electrophysiol | RyR2 通道抑制決定 I 類抗心律不整藥在 CPVT 的療效 |
| [26121139](https://pubmed.ncbi.nlm.nih.gov/26121139/) | 2015 | 前臨床/機轉 | PLoS One | RyR2 活性決定 flecainide 與 R-propafenone 對抗鈣波的效力 |
| [21798265](https://pubmed.ncbi.nlm.nih.gov/21798265/) | 2011 | 前臨床/機轉 | J Mol Cell Cardiol | 篩選 I 類抗心律不整藥對 casq2 缺失心肌細胞鈣波的抑制作用 |
| [30820400](https://pubmed.ncbi.nlm.nih.gov/30820400/) | 2019 | Case report | HeartRhythm Case Rep | Propafenone 有效治療 CPVT 達 35 年 |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | 系統性回顧 | Life (Basel) | 中國 CPVT 患者的臨床特徵、基因與心律不整結果 |
| [39564160](https://pubmed.ncbi.nlm.nih.gov/39564160/) | 2024 | Cohort | Ann Pediatr Cardiol | CPVT 超過 10 年的長期追蹤 |
| [23965883](https://pubmed.ncbi.nlm.nih.gov/23965883/) | 2013 | Cohort | Zhongguo Dang Dai Er Ke Za Zhi | CPVT 的心室心律不整預測因子與藥物療效 |

其餘預測方向（嬰兒持續性心室心搏過速、ARVC）也有少量文獻，多為老舊的觀察性報告，且 ARVC 方向以安全疑慮為主。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67615 | RHYNORM TABLETS 150MG | 未提供 | 未提供 |
| HK-57117 | PROPAFENONE TAB 150MG | 未提供 | 未提供 |
| HK-51473 | APO-PROPAFENONE TAB 150MG | 未提供 | 未提供 |
| HK-59678 | SOBIRAL TAB 150MG | 未提供 | 未提供 |
| HK-14516 | RYTMONORM TAB 150MG | 未提供 | 未提供 |

---

## 安全性考量

**禁忌症（來自知識圖譜的藥物-疾病禁忌關聯，非仿單內容）：**
- 心律相關：長 QT 症候群、尖端扭轉型心室心搏過速
- 心血管：心肌梗塞、冠狀動脈疾病、動脈粥狀硬化、低血壓
- 肝腎：腎臟病、肝病、膽囊疾病
- 血液：顆粒球缺乏症、嗜中性白血球低下症、血紅素病變
- 神經肌肉：重症肌無力
- 電解質：缺鉀

**藥物交互作用：** 共查得 100 筆，以下為部分重點。
- 嚴重（Major）：Dolasetron、Eliglustat
- 中度（Moderate）：Clarithromycin、Cimetidine、Famotidine、Bupropion、Levofloxacin、Ondansetron、Palonosetron、Aprepitant 等

多種交互作用與 QT 延長或 CYP 代謝有關，併用時需特別留意。

**其他注意：** 在 CPVT、嬰兒心搏過速與 ARVC 的文獻中，反覆出現促心律不整與 QRS 增寬的風險，結構性心臟病患者尤需謹慎。
完整警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（躁症）；CPVT 與嬰兒持續性心室心搏過速列為研究問題**

**理由：**
- 排名第一的躁症預測缺乏臨床證據，且現有文獻顯示 Propafenone 反而可能誘發躁症與精神症狀，不建議推進。
- CPVT 有合理的 RyR2 機轉與前臨床證據，但缺少臨床試驗，僅有個案與世代研究，適合作為後續研究問題，而非立即推進。

**若要推進需要：**
- 補齊香港仿單的警語、禁忌與核准適應症資料（目前為阻擋性資料缺口）
- 補充 Propafenone 的作用機轉資料
- 針對 CPVT 設計與 flecainide 比較的前瞻性研究，或系統性整理既有病例
- 建立結構性心臟病、QT 延長與兒童族群的促心律不整風險監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

