---
layout: default
title: Melphalan
parent: 僅模型預測 (L5)
nav_order: 560
evidence_level: L5
indication_count: 6
monitor_inn: "MELPHALAN"
predicted_indications: ["female breast carcinoma", "rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma"]
last_modified_at: 2026-10-28
description: "Melphalan：預測新適應症為女性乳癌 (female breast carcinoma)（證據等級 L2）。原適應症：卵巢癌"
---

# Melphalan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Melphalan：從卵巢癌到女性乳癌
{: .text-alpha }

## 一句話總結

Melphalan 是一種烷化劑類化療藥物，在知識圖譜中記錄的原適應症為卵巢癌及相關卵巢腫瘤。
TxGNN 模型預測它可能對**女性乳癌 (female breast carcinoma)** 有效，
目前有 **3 個臨床試驗**和 **20 篇文獻**與此方向相關，但多為高劑量合併幹細胞移植的早期研究或舊文獻。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 卵巢癌（知識圖譜記錄的關聯；香港許可證資料中未載明核准適應症文字） |
| 預測新適應症 | 女性乳癌 (female breast carcinoma) |
| TxGNN 預測分數 | 0.9967 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。不過 Melphalan 屬於雙功能氮芥類烷化劑，一般認為它透過使 DNA（鳥嘌呤 N7、腺嘌呤 N3）交聯，造成 DNA 斷裂並誘發細胞凋亡。這種細胞毒性機制不具腫瘤類型特異性，因此對乳癌有作用在生物學上是合理的。

在乳癌方面，已有高劑量 Melphalan 合併自體幹細胞救援的研究，也有細胞株（MDA-MB-231）與異種移植的前臨床報告顯示抗腫瘤活性。早期還有一項隨機試驗比較 Melphalan 與 vinorelbine 用於蒽環類藥物難治性晚期乳癌。

但這些證據多來自高劑量、需移植支持的晚期患者，與現行標準乳癌治療相比，效益與風險的平衡並不清楚。骨髓抑制與續發性惡性腫瘤是重要顧慮。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | 完成 | 25 | 劑量遞增 Melphalan 合併自體幹細胞支持與 amifostine 保護，用於癌症患者；僅支持可行性與毒性評估 |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | 終止 | 12 | 第 IV 期乳癌雙次序自體骨髓移植合併 Samarium-153；Melphalan 可能為高劑量療程之一，貢獻無法區分 |
| [NCT00523809](https://clinicaltrials.gov/study/NCT00523809) | Phase 2 | 終止 | 5 | 非清髓性異體移植合併 bevacizumab 用於晚期實體瘤；樣本極小，無可解讀的療效訊號 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7595708](https://pubmed.ncbi.nlm.nih.gov/7595708/) | 1995 | 隨機試驗 | J Clin Oncol | 比較 vinorelbine 與 Melphalan 用於蒽環類難治性晚期乳癌 |
| [6991733](https://pubmed.ncbi.nlm.nih.gov/6991733/) | 1980 | 輔助化療比較 | JAMA | 第 II/III 期乳癌術後比較 Melphalan 與 CFP 方案（173 人） |
| [7042073](https://pubmed.ncbi.nlm.nih.gov/7042073/) | 1982 | 追蹤研究 | Cancer | Melphalan 單藥組早期復發率高於多藥方案 |
| [12189532](https://pubmed.ncbi.nlm.nih.gov/12189532/) | 2002 | Phase II | Bone Marrow Transplant | 轉移性乳癌序貫高劑量 paclitaxel、Melphalan 等療程合併幹細胞支持 |
| [6203662](https://pubmed.ncbi.nlm.nih.gov/6203662/) | 1984 | 單臂研究 | Cancer Chemother Pharmacol | Mitomycin C、Melphalan、methotrexate 組合用於轉移性乳癌，可評估者緩解率 40% |
| [10918405](https://pubmed.ncbi.nlm.nih.gov/10918405/) | 2000 | 單臂研究 | Bone Marrow Transplant | 高劑量 busulfan、Melphalan、thiotepa 作為高風險乳癌鞏固治療（121 人） |
| [12732881](https://pubmed.ncbi.nlm.nih.gov/12732881/) | 2003 | 回溯性研究 | Bone Marrow Transplant | 高劑量 thiotepa、Melphalan、carboplatin 加自體移植，27 位轉移性乳癌患者 |
| [9404925](https://pubmed.ncbi.nlm.nih.gov/9404925/) | 1997 | Phase I-II | Bone Marrow Transplant | 高劑量 Melphalan、mitoxantrone、carboplatin 用於晚期卵巢或乳癌 |
| [7602368](https://pubmed.ncbi.nlm.nih.gov/7602368/) | 1995 | Review | J Clin Oncol | 靜脈高劑量 Melphalan 的臨床藥理與試驗回顧 |
| [37596331](https://pubmed.ncbi.nlm.nih.gov/37596331/) | 2023 | 前臨床（體外） | Sci Rep | 薑黃素合併 Melphalan 使 MDA-MB-231 乳癌細胞週期停滯並凋亡 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-03792 | ALKERAN TAB 2MG | 未載明 | 未載明 |
| HK-37994 | ALKERAN FOR INJ 50MG | 未載明 | 未載明 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（氮芥類烷化劑） |
| 骨髓抑制風險 | 高（高劑量療程需幹細胞支持） |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 全血球計數（CBC，含分類與血小板）、肝腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：腎臟疾病、血小板減少、貧血、白血球減少、嗜中性球低下、顆粒球缺乏症、溶血性貧血、間質性肺病、肺纖維化、藥物性肝損傷、血管炎等。
- **續發性惡性腫瘤風險**：文獻指出烷化劑（含 Melphalan）續發惡性腫瘤，尤其急性白血病的比率偏高。
- **藥物交互作用**（共 100 筆，列出部分）：
  - 中度：Amphotericin B（含脂質複合物、膽固醇硫酸鹽及脂質體劑型）
  - 輕度：Cimetidine、Levofloxacin、硫酸鋅、葡萄糖酸鋅
  - 等級未明：Lansoprazole、Dolasetron、Granisetron、Famotidine、阿斯匹靈、Pantoprazole、Morphine、Metformin、Omeprazole、Vancomycin、Prednisone、Simvastatin

仿單的警語與禁忌資料尚未取得，詳細內容請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有針對乳癌的臨床試驗與多篇文獻，包含一項與 vinorelbine 的隨機比較試驗，但多為早期研究、高劑量移植情境與舊文獻；Melphalan 並非現行乳癌標準治療，效益風險不明。
- 骨髓抑制與續發性惡性腫瘤風險顯著，且其他預測適應症（黏液性腺癌類）僅有模型分數，應維持 Hold。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症文字
- 補充詳細作用機轉資料
- 與現行標準乳癌療法進行效益風險比較，並系統性評估高劑量療程的長期療效
- 制定骨髓抑制與續發性惡性腫瘤的監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

