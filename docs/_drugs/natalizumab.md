---
layout: default
title: Natalizumab
parent: 僅模型預測 (L5)
nav_order: 609
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "NATALIZUMAB"
predicted_indications: ["bronchitis", "parapsoriasis", "psoriasis", "severe nonproliferative diabetic retinopathy", "acute lichenoid pityriasis"]
description: "Natalizumab：預測新適應症為Bronchitis（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Natalizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Natalizumab: Bronchitis
{: .text-alpha }

## 一句話總結

Natalizumab 是一種針對 α4 整合素的單株抗體，原本用於克隆氏症、發炎性腸道疾病與多發性硬化症。
TxGNN 模型預測分數最高的新適應症為支氣管炎，但最值得討論的是**乾癬 (Psoriasis)**，因為它是前幾名中唯一有較多文獻可供評估的候選。
目前沒有相關臨床試驗，僅有 **16 篇文獻**，其中多為個案報告與安全性回顧，證據相互矛盾。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Bronchitis |
| TxGNN 預測分數 | 0.9946 |
| 證據等級 | L5（乾癬）；僅有間接與相互矛盾的文獻，無臨床試驗 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold（需先完成安全性與訊號審查，才考慮研究性評估） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Natalizumab 阻斷 α4 整合素，可限制白血球進入組織。乾癬由 T 細胞浸潤皮膚所驅動，因此理論上，阻斷淋巴球運輸可能減輕皮膚發炎。

原適應症（克隆氏症、多發性硬化症）同屬免疫媒介的慢性發炎疾病。文獻指出多發性硬化症患者合併乾癬並不少見，這是預測在生物學上有一定合理性的原因。

不過，文獻結果並不一致。一項 18 位多發性硬化症合併乾癬患者的病例系列顯示，使用 natalizumab 後乾癬有改善。但多篇個案報告卻描述 natalizumab 治療期間新發或惡化的乾癬，包括膿疱型與關節型乾癬。這種矛盾表示模型預測的方向未必成立，甚至可能存在反常反應的風險。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

下表列出與乾癬最相關的文獻（共 16 篇，此處選列 10 篇，依研究類型優先排序）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33589543](https://pubmed.ncbi.nlm.nih.gov/33589543/) | 2021 | 病例系列 | Neurol Neuroimmunol Neuroinflamm | 18 位多發性硬化症合併乾癬患者使用 natalizumab 後，乾癬有改善 |
| [40526577](https://pubmed.ncbi.nlm.nih.gov/40526577/) | 2025 | Review | Dtsch Arztebl Int | 討論多發性硬化症合併乾癬、類風濕性關節炎、發炎性腸道疾病的治療選擇 |
| [35646438](https://pubmed.ncbi.nlm.nih.gov/35646438/) | 2022 | 個案報告 | Dermatol Pract Concept | Natalizumab 誘發手掌與足底膿疱型乾癬 |
| [28905124](https://pubmed.ncbi.nlm.nih.gov/28905124/) | 2018 | 個案報告＋回顧 | Neurol Sci | Natalizumab 治療期間出現關節型乾癬 |
| [30323758](https://pubmed.ncbi.nlm.nih.gov/30323758/) | 2018 | 個案報告＋回顧 | Case Rep Neurol | 33 歲患者於 natalizumab 治療期間出現斑塊型乾癬，探討是否為誘發或惡化 |
| [15955735](https://pubmed.ncbi.nlm.nih.gov/15955735/) | 2005 | Review | Curr Opin Pharmacol | 抗黏附療法與整合素標靶的整體進展 |
| [25448040](https://pubmed.ncbi.nlm.nih.gov/25448040/) | 2015 | Review | Pharmacol Ther | 白血球整合素在白血球募集與發炎疾病治療標靶中的角色 |
| [20298966](https://pubmed.ncbi.nlm.nih.gov/20298966/) | 2010 | Review | Lancet Neurol | JC 病毒相關 PML 的臨床特徵與致病機轉（安全性背景） |
| [24136456](https://pubmed.ncbi.nlm.nih.gov/24136456/) | 2013 | Review | Curr Neurol Neurosci Rep | 多發性硬化症中的 PML；提及 efalizumab（乾癬用藥）因 PML 下市 |
| [19647202](https://pubmed.ncbi.nlm.nih.gov/19647202/) | 2009 | Review | Lancet Oncol | Rituximab、natalizumab、efalizumab 相關 PML 的回顧 |

其餘文獻多為 PML 與生物製劑安全性的回顧，未提供乾癬療效的直接證據。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61519 | TYSABRI CONCENTRATE FOR SOLUTION FOR INFUSION 300MG（製造商：EISAI (HONG KONG) COMPANY LIMITED） | 輸注用濃縮液（依品名判斷） | 資料未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：進行性多灶性白質腦病 (PML)。此資料來自知識圖譜，並非仿單內容。多篇文獻也證實 natalizumab 與 PML 相關，PML 是由 JC 病毒再活化引起的罕見但常致命的腦部疾病。
- **皮膚反常反應**：多篇個案報告顯示 natalizumab 可能誘發或惡化乾癬，也有報告顯示與副乾癬、急性苔癬樣糠疹等皮膚不良事件有關。
- **感染風險**：生物製劑使用與感染風險增加相關，不利於感染性或發炎性呼吸道疾病（如支氣管炎）。
- **藥物交互作用**：資料庫共查得 100 項交互作用，以下為部分重點。
  - **嚴重 (Major)**：皮質類固醇（hydrocortisone、prednisone、prednisolone、dexamethasone、betamethasone、budesonide、triamcinolone）、mercaptopurine、levamisole、trimetrexate，以及放射性藥物（iobenguane I-131、ibritumomab tiuxetan、tositumomab）。
  - **中度 (Moderate)**：naltrexone。
  - **輕微 (Minor)**：各種鋅鹽。

仿單中的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 乾癬的預測缺乏臨床試驗，文獻結果矛盾，既有改善報告，也有誘發或惡化的個案，且伴隨 PML 等重大安全性疑慮。
- 其他預測（支氣管炎、嚴重非增殖性糖尿病視網膜病變）完全無證據支持。副乾癬與急性苔癬樣糠疹僅有同一篇不良事件個案報告，方向反而是風險訊號。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認警語、禁忌與核准適應症。
- 補充詳細的作用機轉資料（MOA）。
- 對乾癬進行系統性的安全性與訊號審查，整合改善與惡化的報告，釐清誰可能受益、誰可能出現反常反應。
- 在確認風險效益後，才考慮設計前瞻性研究，且需納入 PML 風險分層與 JC 病毒監測計畫。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

