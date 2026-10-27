---
layout: default
title: Prilocaine
parent: 僅模型預測 (L5)
nav_order: 731
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Prilocaine：預測新適應症為神經痛 (Neuralgia)（證據等級 L5）。原適應症：早洩 (premature ejaculation)、心因性性交疼痛 (psychologic dyspareunia)"
monitor_inn: "PRILOCAINE"
predicted_indications: ["papillary conjunctivitis", "manic bipolar affective disorder", "bronchitis", "migraine disorder", "neuralgia"]
---

# Prilocaine
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

## Prilocaine：從早洩到神經痛
{: .text-alpha }

## 一句話總結

Prilocaine 是醯胺類局部麻醉藥，常與 lidocaine 組成 EMLA 複方，原本用於早洩與心因性性交疼痛。
TxGNN 模型的最高分預測為乳突性結膜炎，但該預測沒有任何臨床證據；證據最完整的是**神經痛 (Neuralgia)**（分數 99.34%），目前有 **2 個臨床試驗**和 **13 篇文獻**，其中多數為小型或較早期的研究，且以 lidocaine/prilocaine 複方為主。

> 說明：以下各章節的臨床試驗與文獻證據，以證據最完整的「神經痛」為主。TxGNN 排名第 1 的預測為乳突性結膜炎（99.78%），但該預測無臨床試驗與文獻，證據等級為 L5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 早洩 (premature ejaculation)、心因性性交疼痛 (psychologic dyspareunia)（香港許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 神經痛 (Neuralgia)；另有 4 項預測，詳見下文 |
| TxGNN 預測分數 | 99.34%（神經痛）；排名第 1 的乳突性結膜炎為 99.78% |
| 證據等級 | 神經痛 L2（僅有一個小型 Phase 2 開放試驗，嚴格來說未達 L2 的 RCT 標準，偏保守解讀約為 L3）；偏頭痛 L4；其餘 L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Hold（神經痛可列為研究問題，需進一步驗證） |

## 其他預測適應症概覽

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 1 | 乳突性結膜炎 | 99.78% | L5 | Hold |
| 2 | 躁期雙極性情感疾患 | 99.76% | L5 | Hold |
| 3 | 支氣管炎 | 99.64% | L5 | Hold |
| 4 | 偏頭痛 | 99.42% | L4 | Hold |
| 5 | 神經痛 | 99.34% | L2 | Research Question |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Prilocaine 是醯胺類局部麻醉藥，一般認為其作用是阻斷電壓門控鈉離子通道。在神經痛方面，它常以 EMLA（lidocaine 2.5%／prilocaine 2.5%）複方形式使用，可減少異位神經放電與皮膚痛覺感受器的輸入，這在機轉上與神經性疼痛、帶狀疱疹後神經痛有合理關聯。

原適應症（早洩、性交疼痛）同樣與外用麻醉降低局部感覺敏感度有關，與神經痛的「局部感覺傳入下調」邏輯相近。不過現有證據多來自複方產品，無法分離 prilocaine 單方的貢獻。

其他預測則較為薄弱：乳突性結膜炎、支氣管炎、躁症缺乏直接證據，機轉聯結偏推測，且眼部反覆使用局部麻醉藥有毒性疑慮，全身暴露則有高鐵血紅素血症風險。

## 臨床試驗證據

（神經痛）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00916942](https://clinicaltrials.gov/study/NCT00916942) | Phase 2 | 完成 | 20 | 開放標籤，評估帶狀疱疹後神經痛患者在使用 NGX-4010（辣椒素 8% 貼片）前，以 lidocaine/prilocaine 乳膏做預處理的耐受性；屬程序性用途，非主要治療 |
| [NCT06899438](https://clinicaltrials.gov/study/NCT06899438) | N/A | 完成 | 38 | 比較 prilocaine 與 A 型肉毒桿菌毒素用於肌筋膜疼痛症候群，與神經痛僅間接相關 |

偏頭痛另有 [NCT02403687](https://clinicaltrials.gov/study/NCT02403687)（N/A，完成，300 人）：外用非類固醇抗發炎藥鎮痛效果的 24 週觀察性研究，與 prilocaine 用於偏頭痛的關聯未獲證實。

## 文獻證據

（神經痛，列出最相關者）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2616182](https://pubmed.ncbi.nlm.nih.gov/2616182/) | 1989 | 臨床研究 | Pain | 12 名頑固性帶狀疱疹後神經痛患者使用 EMLA，6 小時後疼痛評分顯著改善，並含藥動學資料 |
| [2493878](https://pubmed.ncbi.nlm.nih.gov/2493878/) | 1989 | 臨床研究 | BMJ | Lignocaine-prilocaine 乳膏用於帶狀疱疹後神經痛（無摘要） |
| [1430539](https://pubmed.ncbi.nlm.nih.gov/1430539/) | 1992 | Review | J Dermatol Surg Oncol | EMLA 在多種皮膚手術與程序中安全有效，亦用於帶狀疱疹後神經痛等 |
| [23314014](https://pubmed.ncbi.nlm.nih.gov/23314014/) | 2013 | Review | Curr Opin Support Palliat Care | 慢性傷口相關疼痛的實證處理方法 |
| [8695081](https://pubmed.ncbi.nlm.nih.gov/8695081/) | 1996 | 病例報告 | J Clin Anesth | EMLA 成功治療對其他療法無效的帶狀疱疹後神經痛 |
| [22182397](https://pubmed.ncbi.nlm.nih.gov/22182397/) | 2011 | 臨床研究 | BMC Anesthesiol | 以 lidocaine/prilocaine 乳膏預處理後，辣椒素 8% 貼片在帶狀疱疹後神經痛患者的耐受性 |
| [41777672](https://pubmed.ncbi.nlm.nih.gov/41777672/) | 2026 | 回溯性世代 | Front Aging Neurosci | 比較單用 EMLA 與椎旁神經阻斷加 EMLA，對胸段帶狀疱疹後神經痛辣椒素貼片耐受性的影響 |
| [10342425](https://pubmed.ncbi.nlm.nih.gov/10342425/) | 1999 | 實驗研究 | Pain | EMLA 預處理未能減輕 1% 外用辣椒素引起的疼痛（9 名健康受試者） |
| [12378018](https://pubmed.ncbi.nlm.nih.gov/12378018/) | 2002 | 世代研究 | J Korean Med Sci | 帶狀疱疹後神經痛的預後因素 |
| [7897165](https://pubmed.ncbi.nlm.nih.gov/7897165/) | 1995 | 其他 | J Allergy Clin Immunol | EMLA 乳膏引起過敏性接觸性皮膚炎，prilocaine 可能為致敏原 |

本表僅列出 10 篇；其餘 3 篇為較間接的研究（局部麻醉相關神經損傷、實驗性感覺變化、製劑研究），與本預測關聯較低，未列入。偏頭痛另有 1 篇間接文獻（PMID 37400308，偏頭痛合併多囊卵巢症候群的微血管功能），未評估 prilocaine。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-27892 | EMLA CREAM 5% | 乳膏 | 未載明 |
| HK-65931 | FORTACIN CUTANEOUS SPRAY, SOLUTION 150MG/ML+50MG/ML | 皮膚噴霧液 | 未載明 |
| HK-67286 | LIPROKING CREAM | 乳膏 | 未載明 |
| HK-59758 | EMLO CREAM | 乳膏 | 未載明 |
| HK-59439 | LIPRY CREAM | 乳膏 | 未載明 |

共 13 張有效單方許可證，無已註銷者，上表僅列 5 張。劑型依品名判斷，許可證資料未載明。

## 安全性考量

- **藥物交互作用**：共查得 22 筆，其中多數為 Major。主要包括：
  - 可能增加高鐵血紅素血症風險的藥物：Dapsone（含外用）、Primaquine、Chloroquine、Quinine、Tafenoquine、Sulfasalazine、Rasburicase、Amyl Nitrite、Nitric Oxide、Silver nitrate（外用）、Silver sulfadiazine（外用）
  - 其他局部麻醉藥：Lidocaine（含外用）、Benzocaine（外用）、Cinchocaine（外用）
  - 其他：Metoclopramide（Major）、Morphine liposomal（Moderate）、Hyaluronidase（Minor）
- **知識圖譜標示的禁忌相關疾病**（非仿單內容，僅供參考）：高血壓、癲癇、腎臟與肝臟疾病、膽囊疾病、糖尿病與酮酸中毒、冠狀動脈疾病、心肌梗塞、血紅素異常症、心臟傳導疾病（含房室傳導阻滯）、呼吸衰竭、隅角閉鎖型青光眼、重症肌無力與神經肌肉接合處疾病、丁醯膽鹼酯酶缺乏、心血管疾病、甲狀腺功能亢進（含 Graves 病）等。
- **其他風險**：大面積或反覆使用時有高鐵血紅素血症風險；已有 EMLA 引起過敏性接觸性皮膚炎的報告，prilocaine 可能為致敏原。

本次未取得香港仿單的警語與禁忌資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold（神經痛可列為研究問題）**

**理由：**
- 神經痛有一定證據（小型 Phase 2 開放試驗與 1989 年起的小型研究），但多為 lidocaine/prilocaine 複方，缺乏對照試驗，無法確認 prilocaine 單方的貢獻。其他四項預測幾乎沒有直接證據。
- 香港仿單的警語與禁忌資料、作用機轉資料均缺漏，目前無法完成安全性初篩。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與適應症文字，完成安全性初篩
- 補齊 prilocaine 的作用機轉資料
- 針對帶狀疱疹後神經痛，搜尋或設計 EMLA 對照試驗（對照安慰劑或單方 lidocaine），分離 prilocaine 的貢獻
- 制定高鐵血紅素血症的監測計畫，特別針對 G6PD 缺乏者、嬰幼兒及併用 DDI 清單中藥物的族群
- 確認給藥途徑與現有許可證劑型（乳膏、噴霧）的相容性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

