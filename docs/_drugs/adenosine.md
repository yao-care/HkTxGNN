---
layout: default
title: Adenosine
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Adenosine：預測新適應症為兒茶酚胺敏感性多形性心室心搏過速 (CPVT)（證據等級 L5）。原適應症：心室心搏過速 (ventricular tachycardia)，來源為 TxGNN 知識圖譜"
monitor_inn: "ADENOSINE"
predicted_indications: ["obsolete bundle branch block"]
---

# Adenosine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Adenosine：從心室心搏過速到兒茶酚胺敏感性多形性心室心搏過速

## 一句話總結

Adenosine（腺苷）原本用於心室心搏過速的治療。
TxGNN 模型預測它可能對**兒茶酚胺敏感性多形性心室心搏過速 (Catecholaminergic Polymorphic Ventricular Tachycardia, CPVT)** 有效，
目前**沒有臨床試驗登記**，僅有 **10 篇文獻**，其中只有 1 篇個案報告直接相關（且使用的是 ATP 而非腺苷），整體證據偏弱。

> 說明：模型預測分數最高的是「obsolete bundle branch block（已廢止的束支傳導阻滯）」，但該術語已在疾病本體中被標示為廢止，且機轉上不合理，也完全沒有證據，因此本報告改以證據較多、機轉較合理的 CPVT 作為主要評估對象。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心室心搏過速 (ventricular tachycardia)，來源為 TxGNN 知識圖譜；香港許可證未列出適應症文字 |
| 預測新適應症 | 兒茶酚胺敏感性多形性心室心搏過速 (CPVT) |
| TxGNN 預測分數 | 99.42% |
| 證據等級 | L4（僅有機轉/前臨床研究與個案報告，無臨床試驗） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，腺苷作用於房室結的 A1 受器，可減慢傳導並終止依賴房室結的心搏過速，在心律不整的急性處理中已有使用經驗。

CPVT 是一種遺傳性心室心搏過速，主要由肌漿網鈣離子滲漏（RyR2、CASQ2、TECRL 等基因）所致，並由兒茶酚胺（交感神經刺激）誘發。腺苷具有對抗 β-腎上腺素刺激的抗腎上腺素效應，並可抑制觸發性活動，因此機轉上有合理的推測空間。

不過需要注意：目前唯一直接相關的臨床資料是一篇個案報告，使用的是三磷酸腺苷 (ATP)，而非腺苷本身，兩者並不等同。即使有效，腺苷最多只可能作為急性終止發作的選項，無法取代 CPVT 的標準治療（β 阻斷劑、flecainide、交感神經切除術）。

另外，排名第一的「obsolete bundle branch block」是束支下方（房室結以下）的傳導缺陷，減慢傳導並非治療手段，且該疾病節點已被廢止，這個高分預測很可能是本體論的假象，不是真正的再利用訊號。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

下表依規則優先列出與腺苷/ATP 直接相關者，再列綜述與其他研究（共 10 篇）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | 個案報告 | Heart Rhythm | ATP 終止了 1 名 CPVT 患者的雙向性心室心搏過速 |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | 共識聲明（綜述） | Europace | 歐洲心律學會等組織對心臟電生理藥物激發試驗的診斷角色之共識 |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | 綜述 | J Assoc Physicians India | 結構正常心臟之心室心搏過速的辨識與處置 |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | 綜述 | Paediatr Anaesth | 麻醉科醫師應知的兒童心律不整 |
| [15324613](https://pubmed.ncbi.nlm.nih.gov/15324613/) | 2004 | 綜述 | Curr Treat Options Cardiovasc Med | 暈厥的治療選擇 |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | 病例報告／觀察性 | Heart Rhythm | RyR2 突變之 CPVT 患者心律調節後的異常再極化 |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | 前臨床（體外模型） | J Physiol | 人源心臟－神經微組織顯示 CPVT 亦與交感神經元有關 |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | 前臨床（機轉） | Commun Biol | TECRL 缺失導致心肌細胞粒線體功能異常 |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | 前臨床（基因治療） | Cardiovasc Res | PDE2A 與 PDE4B 基因治療透過改善 cAMP 分區，改善小鼠心衰竭與心律不整 |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | 前臨床（動物） | Sci Transl Med | 肌漿網鈣漏促成心律不整，但不促成心衰竭進展 |

> 除第一篇個案報告外，其餘文獻均未測試腺苷於 CPVT 的療效。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43112 | ADENOSCAN INJ 3MG/ML（Sanofi Hong Kong） | 注射劑 | 資料未提供 |
| HK-18525 | HEPATOSWISS FOR IV INFUSION INJ（Wilcome） | 注射劑 | 資料未提供 |
| HK-18057 | HEPATOSWISS IM INJ（Wilcome） | 注射劑 | 資料未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜，並非仿單內容）：
  - 呼吸系統：慢性阻塞性肺病 (COPD)、氣喘（含內因性、過敏性）、肺氣腫、呼吸衰竭
  - 心臟傳導與節律：房室傳導阻滯、病竇症候群（含家族性）
  - 心臟結構與血流：主動脈瓣狹窄（含瓣膜疾病、瓣上狹窄）、二尖瓣狹窄、肺動脈瓣逆流、急性冠心症、冠狀動脈疾病、心包炎、低血壓疾病
  - 自主神經：自主神經系統疾病、霍納氏症候群
- **藥物交互作用**：共查詢到 100 筆，主要包括：
  - 較高風險 (Major)：Cisapride、Dolasetron、Papaverine
  - 中度 (Moderate)：Famotidine、Clarithromycin、Granisetron、Levofloxacin、Ondansetron、Palonosetron

仿單層級的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何已登記的臨床試驗，唯一直接證據是一篇使用 ATP 的個案報告，其餘多為機轉或前臨床研究，證據等級僅 L4。
- 第一名預測（obsolete bundle branch block）疑為本體論假象，且機轉上不合理。CPVT 雖有合理的抗腎上腺素機轉，但已有標準治療，腺苷最多只可能是急性終止的輔助選項。
- 此外，腺苷在知識圖譜中有多項心肺相關禁忌，安全性評估也尚未完成。

**若要推進需要：**
- 取得腺苷的作用機轉資料（DrugBank）
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性篩選
- 針對腺苷（而非 ATP）於 CPVT 急性終止的臨床或電生理研究，並與標準治療比較
- 確認 CPVT 患者使用腺苷時，是否可能誘發心律不整，並評估其風險
- 釐清「obsolete bundle branch block」預測是否為本體論假象
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

